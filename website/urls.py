from django.urls import path
from . import views




urlpatterns = [
    path('', views.to_gather, name = 'post_list'),
    path('post/<int:pk>/', views.to_gather_list, name = 'post_detail'),

    path('to_gather/', views.to_gather, name = 'to_gather'),
    path('to_gather/<int:pk>/', views.to_gather_list, name = 'to_gather_list'),
    path('to_gather/new/', views.to_gather_new, name = 'to_gather_new'), # 새로운 글 쓰기 위함
    path('to_gather/<int:pk>/edit/', views.to_gather_edit, name = 'to_gather_edit'), # 글 수정 위함

    path('be_together/', views.be_together, name = 'be_together'),
    path('be_together/<int:pk>/', views.be_together_list, name = 'be_together_list'),
    path('be_together/new/', views.be_together_new, name = 'be_together_new'),
    path('be_together/<int:pk>/edit/', views.be_together_edit, name = 'be_together_edit'),

    path('main.html/', views.main, name = 'main'),
    path('come_together.html/', views.come_together, name = 'come_together'),


]
