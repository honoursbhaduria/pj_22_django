from django.shortcuts import render, redirect
from .models import CartItem, Product
from django.http import HttpResponse

def product_list(request):
    products = Product.objects.all()
    return render(request, 'cart/index.html', {'products': products})


def view_cart(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })
def add_to_cart(request, pk):
    product = Product.objects.get(pk=pk)
    cart_item, created = CartItem.objects.get_or_create(
        product=product,
        # Temporarily remove user filter until migration is applied
        defaults={'quantity': 0}
    )
    cart_item.quantity += 1
    cart_item.save()
    return redirect("cart:view_cart")

def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    if cart_item.user == request.user:
        cart_item.delete()
    return redirect('cart:view_cart')


def home(request):
    return HttpResponse("Welcome to the home page!")
