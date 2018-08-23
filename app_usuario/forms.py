from django import forms

from .models import *

class FormClienteAnuncio(forms.ModelForm):
  class Meta:
    model = ClienteAnuncio
    fields = ('valor','fotos','videos', 'ativo', 'auditoria')