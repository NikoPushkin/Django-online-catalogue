from django.http import HttpResponse
from catalogue.models import Category
from django.shortcuts import render
# 
# def base(request):
#     cat = Category.objects.all()
#     return render(request, 'templates/new_base.html', context={'categories': cat})
