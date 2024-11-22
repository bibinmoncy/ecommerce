from . models import cart,cartitem
from .views import c_id

def counter(request):
    item_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            car=cart.objects.filter(cart_id=c_id(request))
            items=cartitem.objects.all().filter(c=car[:1])
            for i in items:
                item_count += i.quantity
        except cart.DoesNotExist:
            item_count = 0
    return dict(item_count=item_count)

