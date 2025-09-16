from django import forms
from .models import EssayOrder

class EssayOrderForm(forms.ModelForm):
    class Meta:
        model = EssayOrder
        fields = [
            "name", "email", "topic", "pages", "deadline",
            "academic_level", "formatting_style", "instructions",
        ]
        widgets = {
            "deadline": forms.DateInput(attrs={"type": "date"}),
            "instructions": forms.Textarea(attrs={"rows": 4}),
        }
