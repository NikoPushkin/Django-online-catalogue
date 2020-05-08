from django.urls import path

from .views import *

urlpatterns = [
    path('', books_list, name="books_list_url"),
    path('<str:slug>/', books_list, name="category_book_url"),
    path('details/create', BookCreater.as_view(), name='create_book_url'),
    path('details/<str:slug>/', book_details, name="book_details_url"),
    path('details/<str:slug>/update/', BookUpdate.as_view(), name="book_update_url"),
    path('details/<str:slug>/delete/', BookDelete.as_view(), name="book_delete_url"),

    path('categories/', categories_list, name="categories_list_url"),
    path('category/create', CategoryCreate.as_view(), name="category_create_url"),
    path('category/<str:slug>/update/', CategoryUpdate.as_view(), name="category_update_url"),
    path('category/<str:slug>/delete/', CategoryDelete.as_view(), name="delete_cat_url"),
    path('creater/', creater_page, name='creater_url')
    ]
