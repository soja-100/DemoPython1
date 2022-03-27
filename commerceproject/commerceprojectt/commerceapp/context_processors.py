from . models import Category4
def menu_links(request):
    links=Category4.objects.all()
    return dict(links=links)
