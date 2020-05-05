from django.urls import path

from college.views import *


urlpatterns = [
    path('list/', get_colleges, name='college-list'),
    path('<college_slug:str>/', get_single_college, name='single-college')
]

