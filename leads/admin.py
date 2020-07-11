from django.contrib import admin

from leads.models import *


admin.site.site_header = 'ExamKhojo'

admin.site.register(Lead)
admin.site.register(FootPrint)
