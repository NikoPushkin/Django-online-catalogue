from django.forms import ModelForm
from .models import Category, Book
from django.core.exceptions import ValidationError


#forms for creation and change items

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['slug', 'title']

    def clean_slug(self):
        new_cat = self.cleaned_data['slug'].lower()

        #some checks befor creation
        if new_cat == 'create':
            raise ValidationError('"create"-slug does not availible. Please, choose another title')
        if Category.objects.filter(slug__iexact=new_cat).count():
            raise ValidationError('{} slug has been already created'.format(new_cat))
        return new_cat


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'title', 'description', 'slug', 'book_cover', 'book_back',
            'first_page', 'artist', 'artist_info', 'main_photo',
            'theme_photo', 'theme_info', 'tags'
            ]

    def clean_slug(self):
        new_cat = self.cleaned_data['slug'].lower()

        #some checks befor creation
        if new_cat == 'create':
            raise ValidationError('"create"-slug does not availible. Please, choose another title')
        return new_cat



































    # title = forms.CharField(max_length=50)
    # slug = forms.CharField(max_length=50)
    #
    # def clean_cat(self):
    #     new_cat = self.cleaned_data['slug'].lower()
    #
    #     if new_cat == 'create':
    #         raise ValidationError("Category may not be 'Create'")
    #     if Category.objects.filter(slug__iexact=slug).count():
    #         raise ValidationError("{} category have already created".format(new_cat))
    #     return new_cat
    #
    # def save(self):
    #     new_cat = Category.objects.create(
    #         title=self.cleaned_data['title'],
    #         slug=self.cleaned_data['slug']
    #         )
    #     return new_cat
