

from django.urls import path
from djangorestapp import views
urlpatterns = [
    path('article/create', views.article_create, name='article-create'),
    path('article/list', views.article_list, name='article-list'),
    path('article/update/<int:article_id>', views.article_update, name='article-update'),
    path('article/delete/<int:article_id>', views.article_delete, name='article-delete'),
    
]