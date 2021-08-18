from django import forms
from .models import CostModel

class CostForm(forms.ModelForm):
    class Meta:
        model = CostModel
        fields = ['ct_onvan','ct_date', 'ct_mablagh', 'ct_desc']