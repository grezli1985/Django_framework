from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('coin/', views.coin_flip, name='coin'),
    path('c/', views.coin_stat, name='coin_stat'),
    path('r/', views.random_number, name='random'),
    path('authors/', views.authors_view, name='authors'),
    path('posts/', views.posts_view, name='posts'),
]
