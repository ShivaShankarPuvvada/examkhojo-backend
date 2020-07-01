from django.contrib import admin

from college.models import *


admin.site.site_header = 'ExamKhojo'

admin.site.register(College)
admin.site.register(Gallery)
admin.site.register(EntranceExam)
admin.site.register(Degree)
admin.site.register(Stream)
admin.site.register(OfficialContact)
