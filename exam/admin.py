from django.contrib import admin

from exam.models import *

admin.site.site_header = 'ExamKhojo'

admin.site.register(Exam)
admin.site.register(ExamDate)
admin.site.register(ExamCutoff)
admin.site.register(Exam)
