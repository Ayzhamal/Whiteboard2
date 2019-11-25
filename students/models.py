from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    # overriding the parent save function to reduce the size of profile pics
    def save(self, *args, **kwargs):
        # call the parent function 
        super().save(*args, **kwargs)
        
        img=Image.open(self.image.path)
        
        if img.height>300 or img.width>300:
            # tuple for profile pic reduced size 
            output_size=(200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)
        
