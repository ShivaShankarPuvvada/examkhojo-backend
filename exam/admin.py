from django.contrib import admin

from exam.models import Exam

admin.site.site_header = 'ExamKhojo'

admin.site.register(Exam)
