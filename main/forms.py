from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django import forms

class UserForm(forms.ModelForm):
    
    username = forms.EmailField(label='E-mail', 
                    widget=forms.TextInput(attrs={'placeholder': 'joe@gmail.com'}))
    firstname = forms.CharField(label='First Name', 
                    widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    lastname = forms.CharField(label='Last Name', 
                    widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    Password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['firstname','lastname','username','Password']
        
        
        