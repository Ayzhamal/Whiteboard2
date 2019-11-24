from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Course(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    
    def __str__(self):
        return self.title
    
class Enrollment(models.Model):
    date_enrolled=models.DateTimeField(default=timezone.now)
    student=models.ForeignKey(User, on_delete=models.CASCADE)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    midterm1=models.IntegerField()
    midterm2=models.IntegerField()
    final=models.IntegerField()
    
    def __str__(self):
        return self.student.username +'-'+ self.course.title