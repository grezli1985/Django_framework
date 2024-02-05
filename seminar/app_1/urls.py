from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('index1', views.index1, name='index1'),
    path('coin/<int:count>/', views.coin_flip, name='coin'),
    path('cube/<int:count>/', views.cube, name='cube'),
    path('digit/<int:count>/', views.digit, name='digit'),
    path('c/', views.coin_stat, name='coin_stat'),
    # path('r/', views.random_number, name='random'),
    path('authors/', views.authors_view, name='authors'),
    path('posts/', views.posts_view, name='posts'),
    path('authors_post/<int:author_id>/', views.authors_post, name='authors_post'),
    path('post/<int:post_id>/', views.post, name='post'),
    path('game/', views.choose_game, name='choose_game'),
    path('author/', views.author_add, name='author'),
    path('post/', views.post_add, name='post'),
]
