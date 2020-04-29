from django.db import models
from django.shortcuts import reverse
from django.utils.text import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=True)
    return new_slug + str(int(time()))

class Book(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
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

    def get_absolute_url(self):
        return reverse('book_details_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('book_update_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    def get_absolute_url(self):
        return reverse('category_book_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('category_update_url', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
