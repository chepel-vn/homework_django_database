from django.shortcuts import render
from phones.models import Phone


def group(lst):
    start = 0
    for i in range(2):
        stop = start + len(lst[i::2])
        yield lst[start:stop]
        start = stop


def show_catalog(request):
    template = 'catalog.html'

    # < имя_сайта > / catalog?sort = name
    value = request.GET.get("sort")

    if value is not None:
        if value == "name":
            objs = Phone.objects.order_by("name")
        elif value == "min_price":
            objs = Phone.objects.order_by("price")
        elif value == "max_price":
            objs = Phone.objects.order_by("-price")
        else:
            objs = Phone.objects.all()
    else:
        objs = Phone.objects.all()

    context = {'phones': objs}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    obj = Phone.objects.filter(slug=slug)

    context = {'phone': obj[0]}
    return render(request, template, context)
