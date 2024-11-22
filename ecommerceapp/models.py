from django.db import models
from django.urls import reverse

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='category_images',blank=True)

    class Meta:
        ordering=('name',)
        verbose_name = 'verbose_category'
        verbose_name_plural = 'verbose_categories'

    def get_url(self):
        return reverse('ecommerceapp:products_by_category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

class product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product_images',blank=True)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('ecommerceapp:prodetail',args=[self.category.slug,self.slug])

    class Meta:
        ordering=('name',)
        verbose_name = 'verbose_product'
        verbose_name_plural = 'verbose_products'

    def __str__(self):
        return '{}'.format(self.name)