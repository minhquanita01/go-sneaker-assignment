<<<<<<< HEAD
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
        return JsonResponse({'error': 'Shoe not found'}, status=404)
    
    cart = request.session.get('cart', {})
    request.session['cart'] = cart
    
    total_cost = sum(GO_Shoes.objects.get(shoesID=id).shoes_price for id in cart)
    
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

    context = {'available_shoes': available_shoes}
=======
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
        return JsonResponse({'error': 'Shoe not found'}, status=404)
    
    cart = request.session.get('cart', {})
    request.session['cart'] = cart
    
    total_cost = sum(GO_Shoes.objects.get(shoesID=id).shoes_price for id in cart)
    
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

    context = {'available_shoes': available_shoes}
>>>>>>> 0d41086a3a90370f94e40901e573e9ddf10d20c3
    return render(request, 'index.html', context)