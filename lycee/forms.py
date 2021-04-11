from django.forms.models import ModelForm
from .models import Student


class StudentForm(ModelForm):
  class Meta:
    #model
    model = Student
    #les champs que l'ont veut traiter
    fields =(
      'first_name',
      'last_name',
      'birth_date',
      'email',
      'phone',
      'cursus',
      'comments',
    )
  