from django.db import models
from django import forms
from members import models as members_models

# Create your models here.
"""
class SomeModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SomeModelForm, self).__init__(*args, **kwargs)
        self.fields['some_field'].widget = forms.CheckboxSelectMultiple()
"""
    
class Period(models.Model):
    student1 = members_models.Person()
    student2 = members_models.Person()



    