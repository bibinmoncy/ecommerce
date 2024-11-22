from django.shortcuts import render, redirect, get_object_or_404
from ecommerceapp.models import product
from .models import cart,cartitem
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def c_id(request):
    c_data=request.session.session_key
    if not c_data:
        c_data=request.session.create()
    return c_data

def add_cart(request,product_id):
    p1=product.objects.get(id=product_id)
    try:
        c1=cart.objects.get(cart_id=c_id(request))
    except cart.DoesNotExist:
        c1=cart.objects.create(cart_id=c_id(request))
        c1.save()
    try:
        c_items=cartitem.objects.get(pr=p1,c=c1)
        if c_items.quantity < c_items.pr.stock:
            c_items.quantity += 1
        c_items.save()
    except cartitem.DoesNotExist:
        c_items=cartitem.objects.create(
            pr=p1,
            quantity=1,
            c=c1
        )
        c_items.save()
    return redirect('cartapp:cart_detail')


def cart_detail(request,total=0,counter=0,c_items=None):
    try:
        c1=cart.objects.get(cart_id=c_id(request))
        c_items=cartitem.objects.filter(c=c1,active=True)
        for i in c_items:
            total += (i.pr.price * i.quantity)
            counter += i.quantity

    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(c_items=c_items,total=total,counter=counter))



def cart_remove(request,product_id):
    c2=cart.objects.get(cart_id=c_id(request))
    p2=get_object_or_404(product,id=product_id)
    cart_items=cartitem.objects.get(pr=p2,c=c2)
    if cart_items.quantity > 1:
        cart_items.quantity -= 1
        cart_items.save()
    else:
        cart_items.delete()
    return redirect('cartapp:cart_detail')


def full_remove(request,product_id):
    c2 = cart.objects.get(cart_id=c_id(request))
    p2 = get_object_or_404(product, id=product_id)
    cart_items = cartitem.objects.get(pr=p2,c=c2)
    cart_items.delete()
    return redirect('cartapp:cart_detail')
