from django.contrib import admin

from college.models import *


admin.site.site_header = 'ExamKhojo'


class GalleryAdmin(admin.TabularInline):
    model = Gallery


class CollegeAdmin(admin.ModelAdmin):
    inlines = [GalleryAdmin, ]


admin.site.register(CollegeAdmin)
admin.site.register(Gallery)
admin.site.register(EntranceExam)
admin.site.register(Degree)
admin.site.register(Stream)
admin.site.register(OfficialContact)
