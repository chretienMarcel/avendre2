from django.contrib import admin
from .models import ProfileModel
# Register your models here.

class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ( "user", "image", "date_created")

admin.site.register(ProfileModel, ProfileModelAdmin)



