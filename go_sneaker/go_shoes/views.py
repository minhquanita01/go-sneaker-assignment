from django.shortcuts import render
from django.http import JsonResponse
from go_shoes.models import GO_Shoes
import json
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string

@require_POST
@csrf_exempt
def add_to_cart(request):
    data = json.loads(request.body)
    shoe_id = data.get('shoe_id')
    try:
        shoe = GO_Shoes.objects.get(shoes_ID = shoe_id)
    except GO_Shoes.DoesNotExist:
        return JsonResponse({'error': 'Shoe not found'}, status = 404)
    
    cart_items = request.session.get('cart_items', [])
    cart_items.append(
        {
            "shoes_ID": shoe.shoes_ID,
            "shoes_image_path": shoe.shoes_image_path,
            "shoes_name": shoe.shoes_name,
            "shoes_price": shoe.shoes_price,
            "shoes_color": shoe.shoes_color,
            "buy_quantity": 1,
        }
    )
    shoe_price = shoe.shoes_price
    total_cost = request.session.get('total_cost', 0)
    total_cost += shoe_price
    request.session['cart_items'] = cart_items
    request.session['total_cost'] = total_cost
    
    cart_item_html = render_to_string('cart_item.html', {'shoe': shoe})
    
    return JsonResponse({'html': cart_item_html, 'total_cost': total_cost})

@require_POST
@csrf_exempt
def inc_quantity_cart(request):
    data = json.loads(request.body)
    shoe_id = data.get('shoe_id')
    
    cart_items = request.session.get('cart_items', [])
    total_cost = request.session.get('total_cost', 0)
    item_quantity = 0
    for item in cart_items:
        if item["shoes_ID"] == int(shoe_id):
            item_quantity = item["buy_quantity"] = item["buy_quantity"] + 1
            total_cost += item["shoes_price"]
            break
    
    request.session['cart_items'] = cart_items
    request.session['total_cost'] = total_cost
    
    return JsonResponse({'total_cost': total_cost, 'item_quantity': item_quantity})

@require_POST
@csrf_exempt
def desc_quantity_cart(request):
    data = json.loads(request.body)
    shoe_id = data.get('shoe_id')
    
    cart_items = request.session.get('cart_items', [])
    total_cost = request.session.get('total_cost', 0)
    item_quantity = 0
    for item in cart_items:
        if item["shoes_ID"] == int(shoe_id):
            item_quantity = item["buy_quantity"] = item["buy_quantity"] - 1
            total_cost -= item["shoes_price"]
            if item_quantity == 0:
                cart_items.remove(item)
            break
    
    request.session['cart_items'] = cart_items
    request.session['total_cost'] = total_cost
    
    return JsonResponse({'total_cost': total_cost, 'item_quantity': item_quantity})

@require_POST
@csrf_exempt
def remove_cart_item(request):
    data = json.loads(request.body)
    shoe_id = data.get('shoe_id')
    
    cart_items = request.session.get('cart_items', [])
    total_cost = request.session.get('total_cost', 0)
    for item in cart_items:
        if item["shoes_ID"] == int(shoe_id):
            total_cost -= (item["buy_quantity"] * item["shoes_price"])
            cart_items.remove(item)
            break
    
    request.session['cart_items'] = cart_items
    request.session['total_cost'] = total_cost
    
    return JsonResponse({'total_cost': total_cost})

def index(request):
    #Fetch only products which has quantity greater than 0 (it means that these products still available in the store)
    available_shoes = GO_Shoes.objects.exclude(shoes_quantity = 0).values
    (
        'shoes_ID',
        'shoes_image_path', 
        'shoes_name', 
        'shoes_description', 
        'shoes_price', 
        'shoes_color'
    )
    #print(available_shoes[0])
    cart_items = request.session.get('cart_items', [])
    total_cost = request.session.get('total_cost', 0)

    context = {
        'available_shoes': available_shoes,
        'cart_items': cart_items,
        'total_cost': total_cost,
        }
    return render(request, 'index.html', context)