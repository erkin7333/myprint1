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
    if request.method == 'POST':
        if form.is_valid() and formset.is_valid():
            try:
                with transaction.atomic():
                    orders = form.save(commit=False)
                    orders.save()
                    for i in formset:
                        data = i.save(commit=False)
                        data.orders = orders
                        data.save()
            except IntegrityError:
                print("Xato------------------>>>>>>>>>>>")
            return redirect("myprint:list")
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
    return render(request, 'main/index.html')

def contact(request):
    return render(request, 'main/contact.html')

def portfolio(request):
    return render(request, 'main/portfolio.html')

def gift_product(request):
    return render(request, 'main/gifts-products.html')

def design(request):
    return render(request, 'main/dizayn.html')

def printing_large(request):
    return render(request, 'main/printing-largeformat.html')

def promotional_products(request):
    return render(request, 'main/promotional-products.html')

def markirovka(request):
    return render(request, 'main/markirovka.html')

def poligraphy_product(request):
    return render(request, 'main/poligraphy-products.html')

def printing_paper(request):
    return render(request, 'main/printing-paper.html')

def printing_textile(request):
    return render(request, 'main/printing-textile.html')

def textile_products(request):
    return render(request, 'main/textile-products.html')

def advertisement(request):
    return render(request, 'main/reklama.html')

def invoice(request):
    return render(request, 'main/invoice.html')


