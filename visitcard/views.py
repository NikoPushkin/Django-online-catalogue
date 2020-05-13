from django.http import HttpResponse
from catalogue.models import Category
from django.shortcuts import render, redirect, reverse


#redirect from the base url view
def redirect_page(request):
    return redirect('/catalogue/home')
