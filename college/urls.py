from django.urls import path

from college.views import *


urlpatterns = [
    path('list/', get_colleges, name='college-list'),
]

