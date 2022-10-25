from django.shortcuts import get_object_or_404, redirect, render
from .help_model import Designe
from .forms import OrderServiceForm


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
    context = {
        'desig': desig
    }
    return render(request, 'main/dizayn.html', context=context)
def printing_paper(request):
    return render(request, 'main/printing-paper.html')


def printing_large(request):
    return render(request, 'main/printing-largeformat.html')

def printing_textile(request):
    return render(request, 'main/printing-textile.html')


def textile_products(request):
    return render(request, 'main/textile-products.html')

def markirovka(request):
    return render(request, 'main/markirovka.html')