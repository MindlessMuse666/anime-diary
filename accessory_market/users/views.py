from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from .forms import UserLoginForm


def login(request: HttpRequest):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            username = request.POST('username')
            password = request.POST('password')
            user = authenticate(
                username=username,
                password=password
            )

            if user:
                login(request, user)

                redirect = HttpResponseRedirect(reverse('main:product'))

                return redirect
    else:
        form = UserLoginForm()

    render_view: HttpResponse = render(
        request,
        'users/login.html',
        {'form': form}
    )
    
    return render_view


def registration(request: HttpRequest):
    render_view: HttpResponse = render(
        request,
        'users/registration.html'
    )
    
    return render_view


def profile(request: HttpRequest):
    render_view: HttpResponse = render(
        request,
        'users/profile.html'
    )
    
    return render_view


def logout(request: HttpRequest):
    pass
    # render_view: HttpResponse = render(
    #     request,
    #     'users/login.html'
    # )
    
    # return render_view