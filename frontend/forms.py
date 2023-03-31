from django import forms
from django.forms import Modelform
from .models import Logo

class Logoform(Modelform):
    class Meta:
        model = Logo
        fields = ('logo_image')
        labels = {
            'logo_image': '',
        }