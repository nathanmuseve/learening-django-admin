from django.urls import path
from . import views

urlpatterns = [
    path('library/', views.book_list, name='book_list'),
    path('library/book_detail', views.book_detail, name='book_detail' ),
    path('library/<int:pk>/', views.book_detail_pk, name='book_detail'),
]
