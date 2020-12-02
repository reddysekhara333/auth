from django.contrib import admin

# Register your models here.
from webapp.models import movie
class movieadmin(admin.ModelAdmin):
    list_display = ['date','moviename','hero','heroine','ratings']

admin.site.register(movie,movieadmin)