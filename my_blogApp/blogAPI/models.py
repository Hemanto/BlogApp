from django.db import models
from django.db.models.signals import pre_save
from my_blogApp.utils import unique_slug_generator
from taggit.managers import TaggableManager
from django.utils import timezone
from django.forms.widgets import CheckboxSelectMultiple
from ckeditor.fields import RichTextField

class Category(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.slug


def category_slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(category_slug_generator, sender=Category)


class SubCategory(models.Model):
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.slug


def subcategory_slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(subcategory_slug_generator, sender=SubCategory)


class Blog(models.Model):
    category = models.ManyToManyField(Category)
    subcategory = models.ManyToManyField(SubCategory)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, null=True, blank=True)
    cover_image = models.ImageField(upload_to='blog/cover_image')
    alt_tag = models.CharField(max_length=50,null=True)
    caption = models.CharField(max_length=200)
    Image_Credit = models.CharField(max_length=200)
    intro = models.TextField()
    description = models.TextField()
    body = RichTextField(blank=True, null=True)
    seo_title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=100)
    place = models.CharField(max_length=50)
    STATUS = (
        ('Publish', 'Publish'),
        ('Draft', 'Draft')
    )
    status = models.CharField(choices=STATUS, default='Publish', max_length=7)
    tag = TaggableManager()
    date = models.CharField(max_length=50,null=True)
    premium = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title



def blog_slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(blog_slug_generator, sender=Blog)

