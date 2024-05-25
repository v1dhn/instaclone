from django import forms
from .models import User

class UserSignUpForm(forms.ModelForm):

    name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={
            "placeholder":"Provide your full name",
            "class":"input-fields"
        }),
        label="Full Name"
    )

    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(
        attrs={
            "placeholder":"Provide your email",
            "class":"input-fields"
        }),
        label="Email")
    
    password = forms.CharField(required=True, widget=forms.widgets.PasswordInput(
        attrs={
            "placeholder":"Enter password",
            "class":"input-fields"
        }
    ),label="Password")

    class Meta:
        model = User
        exclude = ('created_on','updated_on','is_active','phone_number')