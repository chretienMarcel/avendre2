from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
statut = (
    ("à louer", "à louer"),
    ("à vendre", "à vendre")
)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=500, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    statut = models.CharField(max_length=20, choices=statut, default="à louer")
    chambres = models.IntegerField(null=False, blank=False)
    telephone = models.CharField(null=False, blank=False, max_length=12)  # Utilisez CharField pour les numéros de téléphone
    prix_en_fbu = models.IntegerField(null=False, blank=False, default=0)
    image1 = models.ImageField(default='default.png', upload_to='post', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    image2 = models.ImageField(default='default.png', upload_to='post', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    image3 = models.ImageField(default='default.png', upload_to='post', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    image4 = models.ImageField(default='default.png', upload_to='post', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])
    image5 = models.ImageField(default='default.png', upload_to='post', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-date_created',)

class Suggestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    facilite_utilisation = models.TextField()  # Question 1
    appreciations = models.TextField()  # Question 2
    problèmes = models.TextField()  # Question 3
    suggestions = models.TextField()  # Question 4
    note = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Note sur 5

    def __str__(self):
        return f'Suggestion de {self.user.username}'

from django.db import models
from django.contrib.auth.models import User
from .models import Post  # Assurez-vous d'importer le modèle Post

class Favoris(models.Model):
    id = models.AutoField(primary_key=True)  # Champ id auto-généré
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)  # Date de création

    class Meta:
        unique_together = ('user', 'post')  # Assure qu'un utilisateur ne peut ajouter qu'une seule fois un post aux favoris

    def __str__(self):
        return f'Favori de {self.user.username} - {self.post.id}'