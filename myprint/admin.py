from django.contrib import admin
from .models import *
from .help_model import Image, Designe, DigitalPrint, TextPrint, LaserPrint, LargeFormat, Type, OrderService
from modeltranslation.admin import TranslationAdmin

# Register your models here.
@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = [
        'category', 'name', 'image', 'info_product',
        'vendor_code', 'description'
    ]
    list_display_links = [
        'category', 'name'
    ]
    list_per_page = 2


class OrderAdmin(admin.TabularInline):
    model = Order
    fields = [
        'name', 'amount'
    ]


class UserOrderAdmin(admin.ModelAdmin):
    inlines = [OrderAdmin]


admin.site.register(UserOrder, UserOrderAdmin)
admin.site.register(Order)


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = [
        'id', 'parent', 'name', 'image'
    ]
    list_display_links = [
        'parent', 'name',
    ]
    list_per_page = 2


class SettingsAdmin(admin.ModelAdmin):
    list_display = [
        'key',
        'value'
    ]
    list_per_page = 2
    class Meta:
        model = Settings


admin.site.register(Settings, SettingsAdmin)


@admin.register(TypeService)
class TypeServiceAdmin(TranslationAdmin):
    list_display = [
        'name', 'image'
    ]
    list_display_links = [
        'name'
    ]
    list_per_page = 2



@admin.register(MenuService)
class MenuServiceAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'image',
        'type_service'
    ]
    list_display_links = [
        'name'
    ]
    list_per_page = 2



@admin.register(About)
class AboutAdmin(TranslationAdmin):
    list_display = [
        "description"
    ]
    list_display_links = [
        "description"
    ]
    list_per_page = 2


@admin.register(AboutImage)
class AboutImageAdmin(TranslationAdmin):
    list_display = [
        "name", "image"
    ]
    list_display_links = [
        "name",
    ]
    list_per_page = 2



class OrderServiceAdmin(admin.ModelAdmin):
    list_display = [
        'order_type', 'username', 'phone_number',
        'creat_add'
    ]
    list_display_links = [
        'order_type', 'username'
    ]

    class Meta:
        model = OrderService


admin.site.register(OrderService, OrderServiceAdmin)


@admin.register(Type)
class TypeAdmin(TranslationAdmin):
    list_display = ['name']
    list_display_links = ['name']



class ImageAdmin(admin.ModelAdmin):
    list_display = [
        'type_sevice', 'image'
    ]
    list_display_links = [
        'type_sevice',
    ]
    list_per_page = 2
    class Meta:
        model = Image


admin.site.register(Image, ImageAdmin)


@admin.register(Designe)
class DesigneAdmin(TranslationAdmin):
    list_display = [
        'description',
        'image1', 'image2', 'image3'
    ]
    list_display_links = ['description']


@admin.register(DigitalPrint)
class DigitalPrintAdmin(TranslationAdmin):
    list_display = [
        'description', 'size',
        'type', 'on_site_print', 'double_site_print', 'image'
    ]
    list_display_links = ['size', 'type']



@admin.register(LargeFormat)
class LargeFormatAdmin(TranslationAdmin):
    list_display = [
       'description', 'product_name',
        'type', 'price', 'image1', 'image2', 'image3'
    ]
    list_display_links = ['product_name']


@admin.register(TextPrint)
class TextPrintAdmin(TranslationAdmin):
    list_display = [
        'size', 'price',
        'description', 'image'
    ]
    list_display_links = ['size', 'price']


@admin.register(LaserPrint)
class LaserPrintAdmin(TranslationAdmin):
    list_display = [
        'size', 'price',
        'description', 'image'
    ]
    list_display_links = ['size', 'price']
