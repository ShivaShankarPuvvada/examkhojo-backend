from django.urls import path

from course.views import *


urlpatterns = [
    path('list/', get_courses, name='college-list'),
    path('<course_slug>/', get_single_course, name='single-course')
]

