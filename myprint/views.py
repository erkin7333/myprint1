from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .models import UserOrder, Order
from .forms import UserOrderForm, OrderForm, OrderServiceForm, Product_OrdersForm
from django.shortcuts import redirect
from django.forms import modelformset_factory
from django.core.paginator import Paginator
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
    form = OrderServiceForm()
    if request.method == 'POST':
        form = OrderServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form': form,
        "servistype": servistype,
        "menuservice": menuservice,
    }
    return render(request, 'main/index.html', context=context)


def servicecategory(request, pk):
    page_service = MenuService.objects.filter(type_service_id=pk)
    paginator = Paginator(page_service, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj
    }
    return render(request, 'main/service_page.html', context=context)


def contact(request):
    return render(request, 'main/contact.html')


def parent_product(request, id):
    product = Product.objects.filter(category__parent_id=id)
    print("Parent Filter--------------->>>>>>>>>>>>", product)
    form = Product_OrdersForm()
    if request.method == 'POST':
        form = Product_OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myprint:home')
        else:
            form = Product_OrdersForm()
    context = {
        'product': product,
        'form': form,
        'id': id
    }
    return render(request, 'main/gifts-products.html', context=context)


def promotional_products(request):
    return render(request, 'main/promotional-products.html')


def poligraphy_product(request, pk):
    product = Product.objects.filter(category_id=pk)
    form = Product_OrdersForm()
    if request.method == 'POST':
        form = Product_OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myprint:home')
        else:
            form = Product_OrdersForm()
    context = {
        "product": product,
        'form': form,
        'pk': pk
    }
    return render(request, 'main/poligraphy-products.html', context=context)



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
