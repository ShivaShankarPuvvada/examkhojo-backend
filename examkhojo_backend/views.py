from django.shortcuts import render


def get_home(request):
    """Get index page."""
    return render(request, 'dist/index.html')