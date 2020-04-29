from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from .utils import DetailObjectMixin, CreateObjectMixin
from .models import Book, Category
from .forms import CategoryForm, BookForm


def books_list(request):
    books = Book.objects.all()
    return render(request, 'catalogue/index.html', context={'books': books})


class BookDetails(DetailObjectMixin, View):
    model = Book
    template = "catalogue/book_details.html"


class BookCategory(DetailObjectMixin, View):
    model = Category
    template = "catalogue/book_category.html"


class CategoryCreate(CreateObjectMixin, View):
    form = CategoryForm
    template = 'catalogue/category_create.html'


class CategoryDelete(View):
    def post(self, request, slug):
        cat_for_del = get_object_or_404(Category, slug__iexact=slug)
        cat_for_del.delete()
        return redirect('/catalogue/categories/')


class BookCreater(CreateObjectMixin, View):
    form = BookForm
    template = 'catalogue/book_create.html'


def categories_list(request):
    categories = Category.objects.all()
    return render(
        request, 'catalogue/categories_list.html',
        context={"categories": categories}
        )

def creater_page(request):
    return render(request, 'catalogue/creater_page.html')
