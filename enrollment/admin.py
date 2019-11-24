from django.contrib import admin
from django.contrib.auth.models import User
from .models import Course, Enrollment

@admin.register(Course, Enrollment)
class Admin(admin.ModelAdmin):
    pass