from django.urls import path
from . import views




urlpatterns = [
    path('to_gather/', views.to_gather, name = 'to_gather'),
    path('to_gather/<int:pk>/', views.to_gather_list, name = 'to_gather_list'),
    path('to_gather/new/', views.to_gather_list_new, name='to_gather_list_new'),
    path('to_gather/<int:pk>/edit/', views.to_gather_list_edit, name='to_gather_list_edit'),
]
