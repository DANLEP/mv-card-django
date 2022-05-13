from django import forms

from landing.models import Application


class CreateApplication(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Application
        fields = ['first_name', 'last_name', 'email', 'phone_number']
