from django.shortcuts import render
from ecommerceapp.models import product
from django.db.models import Q
# Create your views here.


def search(request):
    p=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        p=product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))

    return render(request,'search.html',{'query':query,'p':p})