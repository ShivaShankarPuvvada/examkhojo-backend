from django.contrib import admin

from course.models import *


admin.site.site_header = 'ExamKhojo'

admin.site.register(Course)
admin.site.register(CourseJob)
admin.site.register(Job)
