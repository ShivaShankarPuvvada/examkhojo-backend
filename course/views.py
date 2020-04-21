from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from course.models import Course


def get_courses(request):
    """Get the courses."""
    page = request.GET.get('page', 1)
    search_string = request.GET.get('q', None)
    if search_string:
        course_list = Course.objects.filter(
            full_name__icontains=search_string
        )
    else:
        course_list = Course.objects.all()

    paginator = Paginator(course_list, 10)
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)
    return render(request, 'dist/courses.html', {'courses': courses})


def get_single_course(request, course_slug):
    """Get single course."""
    course = Course.objects.filter(slug=course_slug)
    return render(request, 'dist/individual-course.html', {'course': course})
