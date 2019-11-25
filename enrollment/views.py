from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
# classes needed to use class-based views
from django.views.generic import(ListView, DetailView)
from .models import Course, Enrollment


def about(request):
    return render(request, 'enrollment/about.html')

class EnrollmentListView(LoginRequiredMixin, ListView):
    model=Enrollment
    template_name='enrollment/home.html'
    context_object_name='enrollments'
    ordering=['-date_enrolled']
    
    def get_queryset(self):
        user=self.request.user
        return Enrollment.objects.filter(user=user).order_by('-date_enrolled')
    
    # def get_queryset(self):
    #     user=get_object_or_404(User, username=self.kwargs.get('username'))
    #     return Enrollment.objects.filter(user=user).order_by('-date_enrolled')
    
    
class EnrollmentDetailView(LoginRequiredMixin, DetailView):
    model=Enrollment
    
    
    
    
    
    
