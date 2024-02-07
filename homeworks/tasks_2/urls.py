from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('upload/', views.upload_image, name='upload_image'),
    path('user/add/', views.user_form, name='user_form'),
]
