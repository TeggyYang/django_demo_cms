from django.contrib import admin
from pic_app.models import Course, Photo


class PhotoInline(admin.TabularInline):
    model = Photo


class CourseAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Photo)