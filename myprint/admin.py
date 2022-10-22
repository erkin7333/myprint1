from django.contrib import admin
from django_admin_listfilter_dropdown.filters import (
    DropdownFilter, ChoiceDropdownFilter, RelatedDropdownFilter
)
from .models import *
from django.utils.html import format_html


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


class ImageAdmin(admin.ModelAdmin):
    list_display = [
        'type_sevice', 'image'
    ]
    list_display_links = [
        'type_sevice'
    ]
    list_per_page = 2
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


class TypeAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'name_uz', 'name_ru'
    ]
    list_display_links = [
        'name_uz', 'name_ru'
    ]
    list_per_page = 2
    class Meta:
        model = Type


admin.site.register(Type, TypeAdmin)


class TypeAdminService(admin.ModelAdmin):
    readonly_fields = ('photo_tag1', 'photo_tag2', 'photo_tag3')
    list_display = [
        'id', 'size', 'type_paper', 'one_site_print',
        'double_site_print', 'shiroki_size', 'shiroki_name', 'shiroki_price',
        'tekstil_size', 'tekstil_price', 'lazer_size', 'lazer_price',
        'photo_tag1', 'photo_tag2', 'photo_tag3'
    ]
    list_display_links = [
        'size', 'type_paper', 'one_site_print',
        'double_site_print'
    ]
    list_filter = ('type', )
    list_per_page = 1
    def photo_tag1(self, obj):
        return format_html(f'<img src="{obj.image1.url}" style="height:100px; width:100px; border-radius: 50%">')
    def photo_tag2(self, obj):
        return format_html(f'<img src="{obj.image2.url}" style="height:100px; width:100px; border-radius: 50%">')
    def photo_tag3(self, obj):
        return format_html(f'<img src="{obj.image3.url}" style="height:100px; width:100px; border-radius: 50%">')
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
