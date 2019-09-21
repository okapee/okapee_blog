from django.urls import path
from . import views

app_name = 'okapee_diary'  # django2.0から必要になったnamespace定義
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('article/<int:pk>/', views.article, name='article'),
    path('article/create/', views.create_article, name='create_article'),
    path('article/<int:pk>/edit/', views.edit_article, name='edit_article'),
    path('article/<int:pk>/delete', views.delete_article, name='delete_article'),
    path('article/<int:pk>/comment-delete/<int:comment_pk>/', views.delete_comment, name='delete_comment'),
]