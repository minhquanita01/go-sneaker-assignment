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
        shoe = GO_Shoes.objects.get(shoesID = shoe_id)
    except GO_Shoes.DoesNotExist:
        return JsonResponse({'error': 'Shoe not found'}, status = 404)
    
    del request.session['total_cost']

    cart_items = request.session.get('cart_items', [])
    cart_items.append(
        {
            "shoes_ID": shoe.shoesID,
            "shoes_image_path": shoe.shoes_image_path,
            "shoes_name": shoe.shoes_name,
            "shoes_price": shoe.shoes_price,
            "buy_quantity": 1,
        }
    )
    request.session['cart_items'] = cart_items
    
    shoe_price = shoe.shoes_price
    total_cost = request.session.get('total_cost', 0)
    total_cost += shoe_price
    request.session['total_cost'] = total_cost
    
    cart_item_html = render_to_string('cart_item.html', {'shoe': shoe})
    
    return JsonResponse({'html': cart_item_html, 'total_cost': total_cost})

def index(request):
    #Fetch only products which has quantity greater than 0 (it means that these products still available in the store)
    available_shoes = GO_Shoes.objects.exclude(shoes_quantity = 0).values
    (
        'shoes_image_path', 
        'shoes_name', 
        'shoes_description', 
        'shoes_price', 
        'shoes_color'
    )
    cart_items = request.session.get('cart_items', [])
    #del request.session['cart_items']

    context = {
        'available_shoes': available_shoes,
        'cart_items': cart_items,
        }
    return render(request, 'index.html', context)