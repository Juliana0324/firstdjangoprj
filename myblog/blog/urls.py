from django.urls import path
from blog import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    
    # 127.0.0.1:8000/post/1 패턴에 해당하는 path를
    # blog/urls.py에 작성해주세요
    # /post/숫자를 2차 url로 작성해주세요. 1차url은 없습니다.
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

]