from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout
from myprint.models import User
from .forms import UserLoginForm
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def user_login(request):
    if request.method == 'GET':
        print("GET ---------------> ")
        form = UserLoginForm()
        context = {'form': form}
        print(context)
        return render(request, template_name='main/loginpage.html', context=context)
    else:
        form = UserLoginForm(request.POST)

        if form.is_valid():

            user_name = request.POST['phone_number']
            password = request.POST['password']

            print("phone   ", user_name)
            print("password --> ", password)
            user = User.objects.filter(phone_number=user_name).first()

            user = authenticate(phone_number=user_name, password=password)
            print("user --- ", user)
            if user:
                auth_login(request, user)
                print("login ---> ", auth_login)
                return render(request, 'main/successpage.html')
            else:
                return render(request, template_name='main/errorpage.html', context={'login': auth_login})


def user_logout(request):
    logout(request)
    return redirect('myprint:home')