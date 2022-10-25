from django.contrib import admin
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)
from .models import *
from django.utils.html import format_html
from .help_model import Image, Designe, DigitalPrint, TextPrint, LaserPrint, LargeFormat, Type, OrderService


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'category', 'name_uz', 'name_ru', 'image', 'info_product',
        'vendor_code', 'description_uz', 'description_ru'
    ]
    list_display_links = [
        'category', 'name_uz', 'name_ru'
    ]
    list_per_page = 2
    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.TabularInline):
    model = Order
    fields = [
        'name', 'amount'
    ]


class UserOrderAdmin(admin.ModelAdmin):
    inlines = [OrderAdmin]


admin.site.register(UserOrder, UserOrderAdmin)
admin.site.register(Order)


class CategoryAdmin(admin.ModelAdmin):
    fields = [
        'parent', 'name_uz', 'name_ru', 'image'
    ]
    list_display = [
        'id', 'parent', 'name_uz', 'name_ru', 'image'
    ]
    list_display_links = [
        'parent', 'name_uz', 'name_ru',
    ]
    list_per_page = 2
    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)


class SettingsAdmin(admin.ModelAdmin):
    list_display = [
        'key',
        'value'
    ]
    list_per_page = 2
    class Meta:
        model = Settings


admin.site.register(Settings, SettingsAdmin)


class TypeServiceAdmin(admin.ModelAdmin):
    list_display = [
        'name_uz', 'name_ru', 'image'
    ]
    list_display_links = [
        'name_uz', 'name_ru'
    ]
    list_per_page = 2
    class Meta:
        model = TypeService


admin.site.register(TypeService, TypeServiceAdmin)

class MenuServiceAdmin(admin.ModelAdmin):
    list_display = [
        'name_uz', 'name_ru', 'image',
        'type_service'
    ]
    list_display_links = [
        'name_uz', 'name_ru'
    ]
    list_per_page = 2

    class Meta:
        model = MenuService


admin.site.register(MenuService, MenuServiceAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = [
        "description_uz", "description_ru",
    ]
    list_display_links = [
        "description_uz", "description_ru",
    ]
    list_per_page = 2
    class Meta:
        model = About


admin.site.register(About, AboutAdmin)


class AboutImageAdmin(admin.ModelAdmin):
    list_display = [
        "name_uz", "name_ru", "image"
    ]
    list_display_links = [
        "name_uz", "name_ru"
    ]
    list_per_page = 2

    class Meta:
        model = AboutImage


admin.site.register(AboutImage, AboutImageAdmin)


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

class TypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    class Model:
        model = Type
admin.site.register(Type, TypeAdmin)

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

class DesigneAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'slug', 'description',
        'image1', 'image2', 'image3'
    ]
    list_display_links = ['name']

    class Meta:
        model = Designe

admin.site.register(Designe, DesigneAdmin)


class DigitalPrintAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'slug', 'description', 'size',
        'type', 'on_site_print', 'double_site_print', 'image'
    ]
    list_display_links = ['name']

    class Meta:
        model = DigitalPrint

admin.site.register(DigitalPrint, DigitalPrintAdmin)


class LargeFormatAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'slug', 'description', 'product_name',
        'type', 'price', 'image1', 'image2', 'image3'
    ]
    list_display_links = ['name']

    class Meta:
        model = LargeFormat

admin.site.register(LargeFormat, LargeFormatAdmin)

class TextPrintAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'slug', 'size', 'price',
        'description', 'image'
    ]
    list_display_links = ['name']

    class Meta:
        model = TextPrint

admin.site.register(TextPrint, TextPrintAdmin)

class LaserPrintAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'slug', 'size', 'price',
        'description', 'image'
    ]
    list_display_links = ['name']

    class Meta:
        model = LaserPrint

admin.site.register(LaserPrint, LaserPrintAdmin)