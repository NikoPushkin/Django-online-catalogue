from django.shortcuts import get_object_or_404, render, redirect

from .models import *

class DetailObjectMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})


class CreateObjectMixin:
    form = None
    template = None

    def get(self, request):
        form = self.form
        return render(request, self.template, context={'form': self.form})

    def post(self, request):
        if self.form.__name__.lower() == 'categoryform':
            bound_form = self.form(request.POST)
        else:
            bound_form = self.form(request.POST, request.FILES)
            print('FILES PLUS')

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})
