from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    description = forms.CharField(
        label=("description"),
        max_length=150,
        help_text=("Faites une petite description de votre résidence"),
        required=True,  # Rendre ce champ obligatoire
    )
    location = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 37}),
        required=True,  # Rendre ce champ obligatoire
    )
    chambres = forms.IntegerField(
        required=True,  # Rendre ce champ obligatoire
    )
    telephone = forms.CharField(
        max_length=12,
        help_text=("Veuillez entrer un numéro de téléphone (maximum 12 caractères)."),
        error_messages={'max_length': 'Le numéro de téléphone ne peut pas dépasser 12 caractères.'},
        required=True,  # Rendre ce champ obligatoire
    )
    prix_en_fbu = forms.IntegerField(
        required=True,  # Rendre ce champ obligatoire
    )
    
    statut = forms.ChoiceField(
        choices=[
             ("Maison", "Maison"),
             ("Appartement", "Appartement")
        ],
        label="Statut",
        help_text="Merci de remplir toutes les cases avant de poster.",
        required=True,  # Rendre ce champ obligatoire
    )

    # Champs d'image
    image1 = forms.ImageField(required=True)
    image2 = forms.ImageField(required=True)
    image3 = forms.ImageField(required=True)
    image4 = forms.ImageField(required=True)
    image5 = forms.ImageField(required=True)

    class Meta:
        model = Post
        fields = ('location', 'chambres', 'telephone', 'image1', 'image2', 'image3', 'image4', 'image5', 'description', 'prix_en_fbu', 'statut')

    def clean(self):
        cleaned_data = super().clean()
        images = [
            cleaned_data.get('image1'), 
            cleaned_data.get('image2'),
            cleaned_data.get('image3'), 
            cleaned_data.get('image4'),
            cleaned_data.get('image5')
        ]

        # Vérifiez si au moins une des images est présente
        if all(image is None for image in images):
            raise forms.ValidationError("Vous devez télécharger au moins une image.")

        return cleaned_data
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
   