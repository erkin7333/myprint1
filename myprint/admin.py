from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(InfoType)
admin.site.register(Type)
admin.site.register(User)
admin.site.register(Banner)
admin.site.register(InfoProduct)
admin.site.register(Product)
admin.site.register(Printer)
admin.site.register(TypeService)
admin.site.register(MenuService)
admin.site.register(Tariff)
admin.site.register(MenuTariff)
admin.site.register(CEO)
admin.site.register(Sponsors)
admin.site.register(Contact)
admin.site.register(Portfolio)
admin.site.register(SocialMedia)


class OrderAdmin(admin.TabularInline):
    model = Order


class UserOrderAdmin(admin.ModelAdmin):
    inlines = [OrderAdmin]


admin.site.register(UserOrder, UserOrderAdmin)
admin.site.register(Order)


class CategoryAdmin(admin.ModelAdmin):
    fields = [
        'parent_id', 'name_uz', 'name_ru', 'image'
    ]
    list_display = [
        'id', 'parent_id', 'name_uz', 'name_ru', 'image'
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
