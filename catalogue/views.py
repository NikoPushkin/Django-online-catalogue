from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.core.paginator import Paginator

from .utils import CreateObjectMixin, UpdateObjectMixin, DeleteObjectMixin, ObjectsListMixin
from .models import Book, Category
from .forms import CategoryForm, BookForm

from django.contrib.auth.mixins import LoginRequiredMixin


def books_list(request, slug=None):
    categories = Category.objects.all()

    #Search request handler
    search_query = request.GET.get('search', '')
    if search_query:
        books = Book.objects.filter(title__icontains=search_query)
    else:
        books = Book.objects.all()

    # Filter by existing categories (dropdown menu)
    if slug:
        category = Category.objects.get(slug__iexact=slug).books.all()
        book_paginator = Paginator(category, 3)
    else:
        book_paginator = Paginator(books, 6)

    page_number = request.GET.get('page', 1)
    page = book_paginator.get_page(page_number)

    return render(
        request, 'catalogue/new_index.html',
        context={'books': page, 'categories': categories, 'slug': slug, 'search': search_query}
        )

def book_details(request, slug):
    categories = Category.objects.all()
    book = get_object_or_404(Book, slug__iexact=slug)
    return render(
        request, "catalogue/book_details.html",
        context={'book': book, 'categories': categories}
        )

def home_page(request):
    categories = Category.objects.all()
    return render(request, 'catalogue/home_page.html', context={'categories': categories})

class BookCreater(LoginRequiredMixin, CreateObjectMixin, View):
    form = BookForm
    login_url = '/admin/'
    redirect_field_name = 'redirect_to'

class CategoryCreate(LoginRequiredMixin, CreateObjectMixin, View):
    form = CategoryForm
    login_url = '/admin/'
    redirect_field_name = 'redirect_to'
class CategoryDelete(LoginRequiredMixin, DeleteObjectMixin, View):
    model = Category
    url = 'cat_set_url'
    login_url = '/admin/'
    redirect_field_name = 'redirect_to'

class BookDelete(LoginRequiredMixin, DeleteObjectMixin, View):
    model = Book
    url = 'books_set_url'
    login_url = '/admin/'
    redirect_field_name = 'redirect_to'

class CategoryUpdate(LoginRequiredMixin, UpdateObjectMixin, View):
    model = Category
    form = CategoryForm
    login_url = '/admin/'
    redirect_field_name = 'redirect_to'

class BookUpdate(LoginRequiredMixin, UpdateObjectMixin, View):
    model = Book
    form = BookForm
    login_url = '/admin/'
    redirect_field_name = 'redirect_to'

def creater_page(request):
    return render(request, 'catalogue/creater_page.html')

def crup_page(request):
    categories = Category.objects.all()
    return render(
        request, 'catalogue/crup_page.html',
        context={'categories': categories}
        )

class BookList(ObjectsListMixin, View):
    model = Book

class CategoryList(ObjectsListMixin, View):
    model = Category
