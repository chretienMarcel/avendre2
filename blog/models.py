from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    location= models.CharField(max_length=500,null=False,blank=False)
    description= models.CharField(max_length=500,null=False,blank=False)
    chambres=models.IntegerField(null=False,blank=False)
    telephone=models.IntegerField(null=False,blank=False)
    prix_en_fbu=models.IntegerField(null=False,blank=False,default=0)
    image1= models.ImageField(default='default.png',upload_to='post',validators=[FileExtensionValidator(['png','jpg','jpeg'])])
    image2= models.ImageField(default='default.png',upload_to='post',validators=[FileExtensionValidator(['png','jpg','jpeg'])])
    image3= models.ImageField(default='default.png',upload_to='post',validators=[FileExtensionValidator(['png','jpg','jpeg'])])
    image4= models.ImageField(default='default.png',upload_to='post',validators=[FileExtensionValidator(['png','jpg','jpeg'])])
    image5= models.ImageField(default='default.png',upload_to='post',validators=[FileExtensionValidator(['png','jpg','jpeg'])])

    author=models.ForeignKey(User,on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering=('-date_created',)
# models.py


class Suggestion(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    facilite_utilisation = models.TextField()  # Question 1
    appreciations = models.TextField()  # Question 2
    problèmes = models.TextField()  # Question 3
    suggestions = models.TextField()  # Question 4
    note = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Note sur 5

    def __str__(self):
        return f'Suggestion de {self.user.username}'
    


