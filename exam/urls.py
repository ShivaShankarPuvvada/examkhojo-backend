from django.urls import path

from exam.views import *


urlpatterns = [
    path('list/', get_exams, name='college-list'),
    path('<exam_slug>/', get_single_exam, name='single-exam')
]

