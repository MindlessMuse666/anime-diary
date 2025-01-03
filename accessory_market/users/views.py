from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def login(request: HttpRequest):
    render_view: HttpResponse = render(
        request,
        'users/login.html'
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