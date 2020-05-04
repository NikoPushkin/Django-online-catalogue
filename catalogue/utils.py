from django.shortcuts import get_object_or_404, render, redirect, reverse
from .models import *

class DetailObjectMixin:
    model = None
    category = Category.objects.all()
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj, 'categories': self.category})


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

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})

class UpdateObjectMixin:
    model = None
    form = None
    template = None

    def get(self, request, slug):
        object = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form(instance=object)
        return render(
            request, self.template,
            context={self.model.__name__.lower(): object, 'form': bound_form}
            )

    def post(self, request, slug):
        object = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form(request.POST, instance=object)

        if bound_form.is_valid():
            bound_form.save()
            return redirect(object)
        return render(
            request, self.template,
            context={self.model.__name__.lower(): object, 'form': bound_form}
            )

class DeleteObjectMixin:
    model = None
    # template = None
    url = None

    # def get(self, request, slug):
    #     obj = model.objects.get(slug__iexact=slug)
    #     return render(
    #         request, self.template,
    #         context={self.model.__name__.lower(): obj}
    #         )

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.url))
