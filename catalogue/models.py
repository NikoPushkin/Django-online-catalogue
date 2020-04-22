from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    description = models.TextField(blank=True, db_index=True)
    book_cover = models.ImageField(blank=True, null=True)
    book_back = models.ImageField(blank=True, null=True)
    first_page = models.ImageField(blank=True, null=True)
    artist = models.ImageField(blank=True, null=True)
    artist_info = models.TextField(blank=True, db_index=True)
    main_photo = models.ImageField(blank=True, null=True)
    theme_photo = models.ImageField(blank=True, null=True)
    theme_info = models.TextField(blank=True, db_index=True)
    tags = models.ManyToManyField('Category', blank=True, related_name='books')

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('category_book_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
