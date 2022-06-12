from myapp.models import Student
from django import forms

class EmpForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"