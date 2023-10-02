from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django import forms
from .models import UserProfile 

class SignUpUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ('email', 'username', 'password1', 'password2' )

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.TextInput(attrs={'class': 'form-input'}),
            'password2': forms.TextInput(attrs={'class': 'form-input'}),
            # 'avatar': forms.ImageField(),
        }

class SignInUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ('email','password1', )

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.TextInput(attrs={'class': 'form-input'}),
        }




class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'avatar']  

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)

        self.fields['bio'].widget = forms.Textarea(attrs={'rows': 4})
