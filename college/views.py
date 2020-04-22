from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from college.models import College


def get_colleges(request):
    """Get the colleges."""
    page = request.GET.get('page', 1)
    search_string = request.GET.get('q', None)
    if search_string:
        college_list = College.objects.filter(
            full_name__icontains=search_string
        ).order_by('full_name')
    else:
        college_list = College.objects.all().order_by('full_name')

    paginator = Paginator(college_list, 9)
    try:
        colleges = paginator.page(page)
    except PageNotAnInteger:
        colleges = paginator.page(1)
    except EmptyPage:
        colleges = paginator.page(paginator.num_pages)
    return render(
        request,
        'pages/colleges.html',
        {
            'colleges': colleges
        }
    )


def get_single_college(request, college_slug):
    """Get single college."""
    college = College.objects.filter(slug=college_slug)
    return render(request, 'dist/individual-college.html', {'college': college})
