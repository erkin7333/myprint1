from django.contrib import admin
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)
from .models import *


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'category', 'name_uz', 'name_ru', 'image', 'info_product',
        'vendor_code', 'description_uz', 'description_ru'
    ]
    list_display_links = [
        'category', 'name_uz', 'name_ru'
    ]

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

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)


class SettingsAdmin(admin.ModelAdmin):
    list_display = [
        'key',
        'value'
    ]

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

    class Meta:
        model = TypeService


admin.site.register(TypeService, TypeServiceAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = [
        'type_sevice', 'image'
    ]
    list_display_links = [
        'type_sevice'
    ]

    class Meta:
        model = Image


admin.site.register(Image, ImageAdmin)


class MenuServiceAdmin(admin.ModelAdmin):
    list_display = [
        'name_uz', 'name_ru', 'image',
        'type_service'
    ]
    list_display_links = [
        'name_uz', 'name_ru'
    ]

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

    class Meta:
        model = AboutImage


admin.site.register(AboutImage, AboutImageAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name_uz', 'name_ru'
    ]
    list_display_links = [
        'name_uz', 'name_ru'
    ]

    class Meta:
        model = Type


admin.site.register(Type, TypeAdmin)


class TypeAdminService(admin.ModelAdmin):
    list_display = [
        'id', 'size', 'type_paper', 'one_site_print',
        'double_site_print', 'shiroki_size', 'shiroki_name', 'shiroki_price',
        'tekstil_size', 'tekstil_price', 'lazer_size', 'lazer_price',
        'image1', 'image2', 'image3',
    ]
    list_display_links = [
        'size', 'type_paper', 'one_site_print',
        'double_site_print', 'image1'
    ]
    # list_filter = (
    #     ("type", admin.RelatedOnlyFieldListFilter)
    # )

    class Meta:
        model = Type_Services


admin.site.register(Type_Services, TypeAdminService)


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
