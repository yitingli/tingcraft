from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import CraftCrew


class CraftCrewLoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'id': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'id': 'password'}))


class CraftCrewCreateForm(forms.ModelForm):

    error_messages = {
        'duplicate_username': _("A user with that username already exists."),
        'duplicate_email': _("A user with that email already exists."),
        'short_password': _("The password must be at least 5 characters.")
    }

    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'id': 'password'}))

    class Meta:
        model = CraftCrew
        fields = ('email', 'username')

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            CraftCrew.objects.get(email=email)
        except CraftCrew.DoesNotExist:
            return email
        raise forms.ValidationError(self.error_messages['duplicate_email'])

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            CraftCrew.objects.get(username=username)
        except CraftCrew.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 6:
            raise forms.ValidationError(
                self.error_messages['short_password'])
        return password

    def save(self, commit=True):
        user = super(CraftCrewCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.set_registration_complete()
        if commit:
            user.save()
        return user
