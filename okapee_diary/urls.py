from django.urls import path
from . import views

app_name = 'okapee_diary'  # django2.0から必要になったnamespace定義
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('article/<int:pk>/', views.article, name='article'),
    path('article/<int:pk>/comment-delete/<int:comment_pk>/', views.delete_comment, name='delete_comment'),
    path('article/create/', views.create_article, name='create_article'),
]
