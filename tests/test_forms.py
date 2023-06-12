from django.test import TestCase

from news.forms import RedactorCreationForm, RedactorDataUpdateForm


class FormsTests(TestCase):
    def test_redactor_creation_form(self):
        redactor = {
            "username": "iron_man1",
            "password1": "test12345",
            "password2": "test12345",
            "first_name": "Tony",
            "last_name": "Stark",
            "years_of_experience": 5,
        }
        form = RedactorCreationForm(data=redactor)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, redactor)

    def test_years_of_experience_above_100(self):
        years_of_experience = {"years_of_experience": 102}
        form = RedactorDataUpdateForm(years_of_experience)
        self.assertFalse(form.is_valid())

    def test_years_of_experience_below_0(self):
        years_of_experience = {"years_of_experience": -1}
        form = RedactorDataUpdateForm(years_of_experience)
        self.assertFalse(form.is_valid())
