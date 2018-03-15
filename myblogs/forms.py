from django import forms
from .models import ServiceConfig


class ServiceConfigForm(forms.ModelForm):
    class Meta:
        model = ServiceConfig
        fields = ['svc_name']
        labels = {'config': ''}
