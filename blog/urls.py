from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('blog/', views.index, name='blog-index'),
    path('search/', views.recherche, name='search'),
    path('poster/', views.poster, name='poster'),
    path('post_edit/<int:pk>/', views.post_edit, name='blog-post-edit'),
    path('post_delete/<int:post_id>/', views.delete_post, name='delete'),
    path('suggestions/', views.suggestions, name='suggestions'),
    path('suggestions/delete/<int:suggestion_id>/', views.delete_suggestion, name='delete_suggestion'),
    path('favoris/<int:post_id>/', views.toggle_favoris, name='favoris_toggle'),  # Pour ajouter/retirer un post des favoris
      path('favoris/', views.favoris, name='favoris'),  # Pour ajouter/retirer un post des favoris
]