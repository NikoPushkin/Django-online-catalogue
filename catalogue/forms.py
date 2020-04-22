from django import forms
from .models import Category
from django.core.exceptions import ValidationError

class CategoryForm(forms.ModelForm):
    # title = forms.CharField(max_length=50)
    # slug = forms.CharField(max_length=50)

    class Meta:
        model = Category
        fields = ['title', 'slug']


    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Slug may not be "create"')
        if Category.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(
                'Slug must be unique. We have "{}" slug already'.format(new_slug))

        return new_slug
