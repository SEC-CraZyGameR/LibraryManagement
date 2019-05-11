from django.urls import path
from . import views
from .views import (BookListView,
					AddBookCreateView, 
					BookDeleteView,
					BookDetailView,
					BookUpdateView)
from .views import home, booklist

urlpatterns = [
    path('', home, name = 'library-home'),

    path('book/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    path('book/<int:pk>/update', BookUpdateView.as_view(),name='book-update'),

    path('book/new/', AddBookCreateView.as_view(),name='book-create'),

    path('book/<int:pk>/delete/', BookDeleteView.as_view(),name='book-delete'),

    path('booklist/', booklist,name='library-booklist'),
]
