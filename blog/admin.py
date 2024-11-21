from django.contrib import admin
from .models import Post ,Suggestion,Favoris

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['date_created','author','location','statut','description','prix_en_fbu','chambres','telephone']
admin.site.register(Post,PostAdmin)
class SuggestionAdmin(admin.ModelAdmin):
    list_display=['user','facilite_utilisation','appreciations','problèmes','suggestions','note']
admin.site.register(Suggestion,SuggestionAdmin) 
class FavorisAdmin(admin.ModelAdmin):
    list_display=['user','post','date_created'] 
admin.site.register(Favoris,FavorisAdmin)

