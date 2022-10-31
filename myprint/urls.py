from django.urls import path
from .views import *
from .help_views import *
 
app_name = "myprint"

urlpatterns = [
    path('', home, name='home'),

    path('contact/', contact, name='contact'),

    path('portfolio/', portfolio, name='portfolio'),

    path('gift_product/<int:id>/', gift_product, name='gift_product'),

    path('designe/', designe, name='designe'),

    path('printing_large/', printing_large, name='printing_large'),

    path('promotional_products/', promotional_products, name='promotional_products'),

    path('markirovka/', markirovka, name='markirovka'),

    path('poligraphy_product/<int:pk>/', poligraphy_product,  name='poligraphy_product'),

    path('printing_paper/', printing_paper,  name='printing_paper'),

    path('printing_textile/', printing_textile, name='printing_textile'),

    path('textile_products/', textile_products, name='textile_products'),

    path('about-page/', aboutview, name='about_page'),

    path('service/<int:pk>/', servicecategory, name="service_page"),

    path('invoice/', invoice, name='invoice'),

    path('create_order/', create_order, name="create-order"),

    path('create/', create, name='create'),

    path('list/', list_data, name='list'),

    path('typeimage/<int:pk>/', typeimage, name='typeimage'),

]
