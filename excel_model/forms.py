from django import forms
from .models import ExcelModelNew
from .python_excel import field_names

class ExcelModelForm(forms.ModelForm):
    class Meta:
        model=ExcelModelNew
        fields=field_names