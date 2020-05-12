from django.urls import path

from .views import *

urlpatterns = [
    path('home/', home_page, name="home_page_url"),
    path('crup/', crup_page, name='crup_page_url'),
    path('categories_set/', CategoryList.as_view(), name="cat_set_url"),
    path('books_set/', BookList.as_view(), name="books_set_url"),
    path('', books_list, name="books_list_url"),
    path('<str:slug>/', books_list, name="category_book_url"),
    path('details/create', BookCreater.as_view(), name='book_create_url'),
    path('details/<str:slug>/', book_details, name="book_details_url"),
    path('details/<str:slug>/update/', BookUpdate.as_view(), name="book_update_url"),
    path('details/<str:slug>/delete/', BookDelete.as_view(), name="book_delete_url"),

    path('category/create', CategoryCreate.as_view(), name="category_create_url"),
    path('category/<str:slug>/update/', CategoryUpdate.as_view(), name="category_update_url"),
    path('category/<str:slug>/delete/', CategoryDelete.as_view(), name="category_delete_url"),
    path('creater/', creater_page, name='creater_url'),
    ]
