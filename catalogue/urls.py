from django.urls import path

from .views import *

urlpatterns = [
    path('', books_list, name="books_list_url"),
    path('details/<str:slug>/', book_details, name="book_details_url"),
    path('categories/', categories_list, name="categories_list_url"),
    path('category/create', CategoryCreate.as_view(), name="category_create_url"),
    path('category/<str:slug>/', book_category, name="category_book_url"),
]
