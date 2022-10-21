from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .models import UserOrder, Order
from .forms import UserOrderForm, OrderForm
from django.shortcuts import redirect
from django.forms import modelformset_factory
from django.db import transaction, IntegrityError


def create(request):
    context = {}
    OrdersFormSet = modelformset_factory(Order, form=OrderForm)
    form = UserOrderForm(request.POST or None)
    formset = OrdersFormSet(request.POST or None, queryset=Order.objects.none(), prefix='orderform')
    print("ZAKAZ1----------->>>>>>>>>>>>>", formset)
    print("ZAKAZ2----------->>>>>>>>>>>>>", request.POST)
    if request.method == 'POST':
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect("myprint:list")
        else:
            print(form.errors, formset.errors)
    context['formset'] = formset
    context['form'] = form
    return render(request, "main/create.html", context=context)


def list_data(request):
    datas = UserOrder.objects.all()
    return render(request, 'main/list_object.html', {'datas': datas})


def create_order(request):
    author = UserOrder.objects.all()
    formset = OrderForm(request.POST or None)
    if request.method == "POST":
        if formset.is_valid():
            formset.instance = author
            formset.save()
            return redirect("create-order")

    context = {
        "formset": formset
    }
    return render(request, "main/application_order.html", context=context)


def home(request):
    servistype = TypeService.objects.all()
    menuservice = MenuService.objects.all()
    print("Menyu------------>>>>>>>>", menuservice)
    context = {
        "servistype": servistype,
        "menuservice": menuservice
    }
    return render(request, 'main/index.html', context=context)


def servicecategory(request):
    page_service = MenuService.objects.all()
    context = {
        "page_service": page_service
    }
    return render(request, 'main/service_page.html', context=context)


def contact(request):
    return render(request, 'main/contact.html')


def portfolio(request):
    return render(request, 'main/portfolio.html')


def gift_product(request):
    return render(request, 'main/gifts-products.html')


def service_type(request, pk):
    service = Type_Services.objects.filter(type_id=pk)
    image = Image.objects.filter(type_sevice_id=pk)
    context = {
        'service': service,
        'pk': pk,
        'image': image
    }
    return render(request, 'main/service_type.html', context=context)


def printing_large(request):
    return render(request, 'main/printing-largeformat.html')


def promotional_products(request):
    return render(request, 'main/promotional-products.html')


def markirovka(request):
    return render(request, 'main/markirovka.html')


def poligraphy_product(request, pk):
    product = Product.objects.filter(category_id=pk)
    context = {
        "product": product,
        'pk': pk
    }
    return render(request, 'main/poligraphy-products.html', context=context)


def printing_paper(request):
    return render(request, 'main/printing-paper.html')


def printing_textile(request):
    return render(request, 'main/printing-textile.html')


def textile_products(request):
    return render(request, 'main/textile-products.html')


def aboutview(request):
    about = About.objects.all()
    image = AboutImage.objects.all()
    context = {
        "about": about,
        "image": image
    }
    return render(request, 'main/about.html', context=context)


def invoice(request):
    return render(request, 'main/invoice.html')
