from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class ProfileModel(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='profile/default.webp',upload_to='profile',validators=[FileExtensionValidator(['png','jpg','jpeg','webp'])])
    date_created=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
