from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.core.paginator import Paginator

from .utils import CreateObjectMixin, UpdateObjectMixin, DeleteObjectMixin
from .models import Book, Category
from .forms import CategoryForm, BookForm


def books_list(request, slug=None):
    categories = Category.objects.all()

    search_query = request.GET.get('search', '')
    if search_query:
        books = Book.objects.filter(title__icontains=search_query)
    else:
        books = Book.objects.all()

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

class BookCreater(CreateObjectMixin, View):
    form = BookForm
    template = 'catalogue/object_create.html'

class CategoryCreate(CreateObjectMixin, View):
    form = CategoryForm
    template = 'catalogue/object_create.html'

class CategoryDelete(DeleteObjectMixin, View):
    model = Category
    url = 'categories_list_url'

class BookDelete(DeleteObjectMixin, View):
    model = Book
    url = 'books_list_url'

class CategoryUpdate(UpdateObjectMixin, View):
    model = Category
    form = CategoryForm
    template = 'catalogue/cat_update.html'

class BookUpdate(UpdateObjectMixin, View):
    model = Book
    form = BookForm
    template = 'catalogue/book_update.html'

def creater_page(request):
    return render(request, 'catalogue/creater_page.html')

def crup_page(request):
    categories = Category.objects.all()
    return render(request, 'catalogue/crup_page.html', context={'categories': categories})


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'catalogue/categories_list.html', context={'categories': categories})
