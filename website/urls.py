from django.urls import path
from . import views




urlpatterns = [
    path('', views.to_gather, name = 'post_list'),
    path('post/<int:pk>/', views.to_gather_list, name = 'post_detail'),
    path('main.html/', views.main, name = 'main'),

]
