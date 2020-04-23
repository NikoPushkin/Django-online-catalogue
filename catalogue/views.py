from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from .models import Book, Category
from .forms import CategoryForm

# Create your views here.
def books_list(request):
    books = Book.objects.all()
    return render(request, 'catalogue/index.html', context={'books': books})

def book_details(request, slug):
    book = Book.objects.get(slug__iexact=slug)
    return render(request, "catalogue/book_details.html", context={'book': book})

def book_category(request, slug):
    category = Category.objects.get(slug__iexact=slug)
    return render(request, "catalogue/book_category.html", context={'category': category})

class CategoryCreate(View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'catalogue/category_create.html', context={'form': form})

    def post(self, request):
        bound_form = CategoryForm(request.POST)

        if bound_form.is_valid():
            new_cat = bound_form.save()
            return redirect(new_cat)
        return render(request, "catalogue/category_create.html", context={'form': bound_form})

def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'catalogue/categories_list.html', context={"categories": categories})
