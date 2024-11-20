from django.db import models
from django import forms
from django.core.validators import FileExtensionValidator
from .models import Post



class PostForm(forms.ModelForm):
 description = forms.CharField(
        label=("description"),
        max_length=150,
        help_text=("dites si la maison est a louer ou a acheter et fixer le prix"),
    )
 location = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 37}))
 chambres=forms.IntegerField()
 telephone=forms.IntegerField()
 prix_en_fbu=forms.IntegerField()

 class Meta:
        model = Post  # Cela doit être un modèle
        fields = ('location','chambres','telephone', 'image1', 'image2', 'image3', 'image4', 'image5','description','prix_en_fbu')

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post  # Cela doit être un modèle
        fields = ('location','chambres','telephone', 'image1', 'image2', 'image3', 'image4', 'image5','description','prix_en_fbu')
# blog/forms.py
from django import forms
from .models import Suggestion

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['facilite_utilisation','appreciations','problèmes','suggestions','note']
        widgets = {
            'facilite_utilisation': forms.Textarea(attrs={'placeholder': 'Comment évaluez-vous la facilité d\'utilisation de l\'application ?'}),
            'appreciations': forms.Textarea(attrs={'placeholder': 'Quelles fonctionnalités appréciez-vous le plus ?'}),
            'problèmes': forms.Textarea(attrs={'placeholder': 'Avez-vous rencontré des problèmes lors de l\'utilisation de l\'application ?'}),
            'suggestions': forms.Textarea(attrs={'placeholder': 'Quelles améliorations suggéreriez-vous ?'}),
            'note': forms.RadioSelect(),  # Utilisé pour afficher les étoiles
        }
   