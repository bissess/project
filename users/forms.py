from datetime import date

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, PasswordResetForm, \
    SetPasswordForm

from .models import User


class UserAuthForm(AuthenticationForm):
    username = forms.CharField(label='Username',
                               widget=forms.TextInput(attrs={'class': 'username__input'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'password__input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class UserRegForm(UserCreationForm):
    first_name = forms.CharField(label='First Name',
                                 widget=forms.TextInput(attrs={'class': 'reg__first-name__input'}))
    last_name = forms.CharField(label='Last Name',
                                widget=forms.TextInput(attrs={'class': 'reg__last-name__input'}))

    username = forms.CharField(label='Username',
                               widget=forms.TextInput(attrs={'class': 'reg__username__input'}))
    email = forms.EmailField(label='Email',
                             widget=forms.EmailInput(attrs={'class': 'reg__email__input'}))

    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'reg__password__input'}))
    password2 = forms.CharField(label='Repeat Password',
                                widget=forms.PasswordInput(attrs={'class': 'reg__repeat-password__input'}))

    gender = forms.CharField(label='Gender',
                             widget=forms.Select(choices=User.GENDER_CHOICES,
                                                 attrs={'class': 'gender__input'}))
    date_birthday = forms.DateField(label='Date of birth',
                                    widget=forms.SelectDateWidget(years=range(1900, date.today().year),
                                                                  attrs={'class': 'birth__input'}))

    error_messages = {
        'password_mismatch': 'Пароли не совпадают.',
        'min_length': 'Минимальная длина пароля должна составлять 8 символов',
        'username': 'Этот никнейм уже занят. Придумайте другой.',
    }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('Такой Email уже существует.')
        return email

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'gender', 'date_birthday']


class UserProfileForm(forms.ModelForm):
    photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'photo-input'}))

    class Meta:
        model = get_user_model()
        fields = ['photo', 'first_name', 'last_name', 'username', 'gender', 'date_birthday', 'date_joined']

        labels = {
            'photo': 'Photo',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'username': 'Username',
            'gender': 'Gender',
            'date_birthday': 'Date Birthday',
            'date_joined': 'Date Joined',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'first-name-input'}),
            'last_name': forms.TextInput(attrs={'class': 'last-name-input'}),
            'username': forms.TextInput(attrs={'class': 'username-input'}),
            'gender': forms.Select(choices=User.GENDER_CHOICES, attrs={'class': 'gender-input'}),
            'date_birthday': forms.SelectDateWidget(years=range(1900, 2024), attrs={'class': 'birthday-input'}),
            'date_joined': forms.TextInput(attrs={'class': 'joined-input', 'readonly': 'readonly'}),

        }


class ProfileSafetyForm(PasswordChangeForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'email'}), required=False)
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput(attrs={'class': 'old_password'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class': 'new_password'}))
    new_password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class': 'confirm_password'}))

    class Meta:
        model = get_user_model()
        fields = ['old_password', 'new_password1', 'new_password2', 'email']


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Your Email', widget=forms.EmailInput(attrs={'class': 'email', 'placeholder': 'Enter your email ...'}))


class UserPasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(label='New password',
                                    widget=forms.PasswordInput(
                                        attrs={'class': 'new_password'}))
    new_password2 = forms.CharField(label='Confirm Password',
                                    widget=forms.PasswordInput(
                                        attrs={'class': 'confirm_password'}))
