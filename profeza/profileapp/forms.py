from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import UserInfo
from django.contrib.auth import authenticate


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'A user with that email already exists')
        return email


class UserProfile(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['name']


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Please enter valid credentials!')
            
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect Password, Please Try Again')
            if not user.is_active:
                raise forms.ValidationError('This User Is Not Active')

            return super(UserLoginForm, self).clean(*args, **kwargs)