import datetime

from django import forms
from .models import Author, Post


class GameTypeForm(forms.Form):
    game_type = forms.ChoiceField(choices=[('C', 'Орел или решка'), ('D', 'кубик'), ('N', 'случайное число')])
    throws_number = forms.IntegerField(min_value=1, max_value=64)


# class AuthorAddForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     bio = forms.CharField()
#     birthday = forms.DateField(initial=datetime.date.today)

class AuthorAddForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'last_name', 'email', 'bio', 'birthday']


# class PostAddFormWidget(forms.Form):
#     title = forms.CharField(max_length=50, widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Введите заголовок статьи'}))
#     content = forms.CharField(max_length=150, widget=forms.TextInput(
#         attrs={'class': 'form-control', 'placeholder': 'Введите текст'}))
#     publish_date = forms.DateTimeField(initial=datetime.datetime.now, widget=forms.DateInput(
#         attrs={'class': 'form-control', 'type': 'date'}))
#     author = forms.ModelChoiceField(queryset=Author.objects.all())
#     is_published = forms.BooleanField(required=False, widget=forms.CheckboxInput(
#         attrs={'class': 'form-check-input'}))


class PostAddFormWidget(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'is_published']

    publish_date = forms.DateTimeField(initial=datetime.datetime.now,
                                       widget=forms.DateInput(attrs={
                                           'class': 'form-control',
                                           'type': 'date'}))
    author = forms.ModelChoiceField(queryset=Author.objects.all().order_by('last_name'))
