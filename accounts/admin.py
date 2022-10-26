from django.contrib import admin
from myprint.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = [
        'first_name', 'full_name', 'phone_number', 'email'
    ]

    list_display_links = [
        'first_name', 'full_name', 'phone_number', 'email'
    ]
    class Meta:
        model = User

admin.site.register(User, UserAdmin)