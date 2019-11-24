"""WhiteBoardProject2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views 
from django.urls import path
from students import views as student_views
from enrollment import views as enrollment_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', student_views.register, name='register' ),
    path('profile/', student_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='students/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='students/logout.html'), name='logout'),
    path('', enrollment_views.home, name='enrollment-home')
         # enrollment_views.StudentCourseListView.as_view(template_name='enrollment-home.html') ,name='enrollment-home'),
]
