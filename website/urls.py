from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('to_gather/', views.to_gather, name='to_gather'),
    path('to_gather/<int:pk>/', views.to_gather_list, name='to_gather_list'),
    path('to_gather/new/', views.to_gather_new, name='to_gather_new'),  # 새로운 글 쓰기 위함
    path('to_gather/<int:pk>/edit/', views.to_gather_edit, name='to_gather_edit'),  # 글 수정 위함
]
