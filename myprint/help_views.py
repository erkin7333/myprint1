from django.shortcuts import get_object_or_404, redirect, render
from .help_model import Designe, Image, DigitalPrint, LargeFormat, TextPrint, LaserPrint
from .forms import OrderServiceForm
from django.core.paginator import Paginator
from .models import Product


# def service_type(request, pk):
#     # service = Type_Services.objects.filter(type_id=pk)
#     # print("Maxsulotlar--------------->>>>>>>>>>>", service)
#     # image = Image.objects.filter(type_sevice_id=pk)
#     form = OrderServiceForm()
#     if request.method == 'POST':
#         form = OrderServiceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/')
#     context = {
#         'form': form,
#         'pk': pk,
#
#     }
#     return render(request, 'main/service_type.html', context=context)


def designe(request):
    desig = Designe.objects.filter()
    image = Image.objects.filter()
    context = {
        'desig': desig,
    }
    return render(request, 'main/dizayn.html', context=context)


def printing_paper(request):
    digitalprint = DigitalPrint.objects.filter()
    form = OrderServiceForm()
    if request.method == 'POST':
        form = OrderServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'digitalprint': digitalprint,
        'form': form
    }
    return render(request, 'main/printing-paper.html', context=context)


def printing_large(request):
    largeformat = LargeFormat.objects.filter()
    form = OrderServiceForm()
    if request.method == 'POST':
        form = OrderServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    contenxt = {
        'largeformat': largeformat,
        'form': form
    }
    return render(request, 'main/printing-largeformat.html', context=contenxt)


def printing_textile(request):
    textprint = TextPrint.objects.filter()
    form = OrderServiceForm()
    if request.method == 'POST':
        form = OrderServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'textprint': textprint,
        'form': form
    }
    return render(request, 'main/printing-textile.html', context=context)


def markirovka(request):
    laserprint = LaserPrint.objects.filter()
    form = OrderServiceForm()
    if request.method == 'POST':
        form = OrderServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'laserprint': laserprint,
        'form': form
    }
    return render(request, 'main/markirovka.html', context=context)


def textile_products(request):
    return render(request, 'main/textile-products.html')


def portfolio(request):
    image = Image.objects.all()
    paginator = Paginator(image, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'main/portfolio.html', context=context)


def typeimage(request, pk):
    t_image = Image.objects.filter(type_sevice_id=pk)
    context = {
        't_image': t_image
    }
    return render(request, 'main/reklamaimage.html', context=context)
