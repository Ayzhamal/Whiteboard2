from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Course(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    
    def __str__(self):
        return self.title
    
class Enrollment(models.Model):
    date_enrolled=models.DateTimeField(default=timezone.now)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    midterm1=models.IntegerField()
    midterm2=models.IntegerField()
    final=models.IntegerField()
    
    def __str__(self):
        return self.user.username +'-'+ self.course.title
    
    def get_absolute_url(self):
        return reverse('enrollment-detail', kwargs={'pk':self.pk})