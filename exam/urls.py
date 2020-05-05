from django.urls import path

from exam.views import *


urlpatterns = [
    path('list/', get_exams, name='college-list'),
    path('<exam_slug:str>/', get_single_exam, name='single-exam')
]

