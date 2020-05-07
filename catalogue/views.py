from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.core.paginator import Paginator

from .utils import DetailObjectMixin, CreateObjectMixin, UpdateObjectMixin, DeleteObjectMixin
from .models import Book, Category
from .forms import CategoryForm, BookForm


def books_list(request):
    books = Book.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(books, 3)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    return render(
        request, 'catalogue/new_index.html',
        context={'books': page, 'categories': categories}
        )


class BookDetails(DetailObjectMixin, View):
    model = Book
    template = "catalogue/book_details.html"


class BookCategory(DetailObjectMixin, View):
    model = Category
    template = "catalogue/book_category.html"


class BookCreater(CreateObjectMixin, View):
    form = BookForm
    template = 'catalogue/book_create.html'


class CategoryCreate(CreateObjectMixin, View):
    form = CategoryForm
    template = 'catalogue/category_create.html'


class CategoryDelete(DeleteObjectMixin, View):
    model = Category
    url = 'categories_list_url'

class BookDelete(DeleteObjectMixin, View):
    model = Book
    url = 'books_list_url'

def categories_list(request):
    categories = Category.objects.all()
    return render(
    request, 'catalogue/categories_list.html',
    context={"categories": categories}
    )


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
