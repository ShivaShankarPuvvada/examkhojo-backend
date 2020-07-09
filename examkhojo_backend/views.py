from django.shortcuts import render


def get_home(request):
    """Get index page."""
    # This is static page (dist/index.html) - working fine (useless)
    # This is a jinja layout (pages/index.html) - not working fine (main part)
    # Also check I can serve pages when DEBUG=True (in dev stage)
    return render(request, 'dist/index.html')