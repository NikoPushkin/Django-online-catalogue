from django.http import HttpResponse
from catalogue.models import Category
from django.shortcuts import render, redirect, reverse

def redirect_page(request):
    return redirect('/catalogue/home')
