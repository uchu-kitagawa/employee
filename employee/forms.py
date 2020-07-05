from django import forms
from .models import Department, Club


class SearchForm(forms.Form):
    club = forms.ModelChoiceField(
        queryset=Club.objects, label="club", required=False,
    )
    department = forms.ModelChoiceField(
        queryset=Department.objects, label="department", required=False,
    )