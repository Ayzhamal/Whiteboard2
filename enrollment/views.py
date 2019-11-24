from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# classes needed to use class-based views
from django.views.generic import(ListView, DetailView)
from .models import Course, Enrollment


def home(request):
    return render(request, 'enrollment/enrollment-home.html')

class StudentCourseListView(ListView):
    model=Enrollment
    template_name='enrollment/enrollment-home.html'
    
    
    def get_queryset(self):
        user=get_object_or_404(User, username=self.kwargs.get('username'))
        return Enrollment.objects.filter(student=user).order_by('-date_enrolled')
    
