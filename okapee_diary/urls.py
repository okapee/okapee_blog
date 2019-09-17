from django.urls import path
from . import views

app_name = 'okapee_diary'  # django2.0から必要になったnamespace定義
urlpatterns = [
    path('', views.post_list, name='post_list'),
]
