from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . models import category,product
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.
# def index(request):
#     return HttpResponse("hai buddy")

def all_products(request,c_slug=None):
    c_page=None
    products_list=None
    if c_slug!=None:
        c_page=get_object_or_404(category,slug=c_slug)
        products_list=product.objects.all().filter(category=c_page,available=True)
    else:
        products_list=product.objects.all().filter(available=True)
    paginator=Paginator(products_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except (EmptyPage,InvalidPage):
        pro=paginator.page(paginator.num_pages)
    return render(request,"cat.html",{"c_page":c_page,"pro":pro})

def prodetail(request,c_slug,p_slug):
    try:
        pro1=product.objects.get(category__slug=c_slug,slug=p_slug)
    except Exception as e:
        raise e
    return render(request,'product_detail.html',{'pro1':pro1})