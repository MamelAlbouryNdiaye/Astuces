from django.contrib import admin
from .models import Projet #+
# Register your models here.

#pour une bonne affichage
class AdminProject(admin.ModelAdmin):
    list_display = ('title','description')


admin.site.register(Projet, AdminProject)