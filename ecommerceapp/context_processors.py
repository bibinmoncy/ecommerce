from . models import category
def menu(request):
    links=category.objects.all()
    return dict(links=links)