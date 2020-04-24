from django.contrib.auth import authenticate, login, logout, user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def login_view(request):
    """Login an user."""
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('user-dashboard'))
    else:
        return render(request, '', {'error': 'Wrong Credentials supplied !'})


def is_user_active(user):
    return user.is_active


@user_passes_test(is_user_active)
def logout_view(request):
    """Logout an user."""
    logout(request)
    return HttpResponseRedirect(reverse('home'))






