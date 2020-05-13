from django.shortcuts import get_object_or_404, render, redirect, reverse
from .models import *
from django.core.paginator import Paginator


class CreateObjectMixin:
    form = None
    template = 'catalogue/object_create.html'

    def get(self, request):
        form = self.form
        return render(request, CreateObjectMixin.template, context={'form': self.form})

    def post(self, request):
        object_name = self.form.__name__.lower()

        if object_name == 'categoryform':
            bound_form = self.form(request.POST)
        else:
            bound_form = self.form(request.POST, request.FILES)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(
            request, CreateObjectMixin.template,
            context={'form': bound_form, 'object_name': object_name}
            )

class UpdateObjectMixin:
    model = None
    form = None
    template = 'catalogue/updater.html'

    def get(self, request, slug):
        object = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form(instance=object)
        return render(
            request, UpdateObjectMixin.template,
            context={self.model.__name__.lower(): object, 'form': bound_form}
            )

    def post(self, request, slug):
        object_name = self.form.__name__.lower()
        object = self.model.objects.get(slug__iexact=slug)
        bound_form = self.form(request.POST, instance=object)

        if bound_form.is_valid():
            bound_form.save()
            return redirect(object)

        return render(
            request, UpdateObjectMixin.template,
            context={
                self.model.__name__.lower(): object,
                'form': bound_form,
                'object_name': object_name
                }
            )

class DeleteObjectMixin:
    model = None
    url = None

    def post(self, request, slug):
        obj = self.model.objects.get(slug__iexact=slug)
        obj.delete()
        return redirect(reverse(self.url))

class ObjectsListMixin:
    model = None
    template = 'catalogue/objects_settings.html'

    def get(self, request):
        obj = self.model.objects.all()
        object_name = self.model.__name__.lower()
        categories = Category.objects.all()

        return render(
            request, ObjectsListMixin.template,
            context={
                object_name: obj,
                'object_name': object_name,
                'categories': categories
                }
            )
