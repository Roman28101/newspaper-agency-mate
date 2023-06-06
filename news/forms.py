from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth.forms import UserCreationForm

from news.models import Redactor


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
        )


class RedactorDataUpdateForm(forms.ModelForm):

    class Meta:
        model = Redactor
        fields = ["first_name", "last_name", "years_of_experience", "img"]




