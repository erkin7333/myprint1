from django.urls import path
from .views import user_login, user_logout

app_name = "accounts"


urlpatterns = [
    path('user_login_view/', user_login, name='login'),

    path('logout/', user_logout, name='logout'),
]
