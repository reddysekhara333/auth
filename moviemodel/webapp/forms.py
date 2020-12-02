from django import  forms
from webapp.models import movie

class fomovie(forms.ModelForm):
    class Meta:
        model=movie
        fields='__all__'