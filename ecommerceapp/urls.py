from django.urls import path
from . import views
app_name='ecommerceapp'
urlpatterns=[
    path('',views.all_products,name='allproducts'),
    path('<slug:c_slug>/',views.all_products,name='products_by_category'),
    path('<slug:c_slug>/<slug:p_slug>/',views.prodetail,name='prodetail'),
    # path('',views.index,name='index'),
]