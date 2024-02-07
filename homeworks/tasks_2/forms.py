from datetime import datetime

from django import forms


class UserForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}))


class ImageForm(forms.Form):
    image = forms.ImageField()
