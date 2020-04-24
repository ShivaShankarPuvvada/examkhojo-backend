from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.urls import reverse

from usermodule.models import Profile, User


def register_view(request):
    """Register an user."""
    name = request.POST.get('name')
    password = request.POST.get('password')
    email = request.POST.get('email')
    username = email
    User.objects.create_user(username=username, password=password)
    user = authenticate(username=username, password=password)
    Profile.objects.create(user=user, full_name=name)
    login(request, user)
    return redirect('home')


def login_view(request):
    """Login an user."""
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('user-dashboard')
    else:
        return render(request, '', {'error': 'Wrong Credentials supplied !'})


def is_user_active(user):
    return user.is_active


@user_passes_test(is_user_active)
def logout_view(request):
    """Logout an user."""
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def dashboard_view(request):
    """Get dashboard of an user."""
    profile = Profile.objects.filter(
        user=request.user
    ).first()
    return render(request, 'pages/dashboard.html', {'profile': profile})



