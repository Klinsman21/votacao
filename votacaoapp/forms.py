from django import forms

from . import models

# Reservation
class CommentsForm(forms.ModelForm):
  # status = forms.ChoiceField(widget=forms.RadioSelect, choices=models.Reservation.STATUS)
  
  class Meta:
    model = models.Comments
    fields = ('comentario', 'leiId')#('__all__')
   

# Reservation
