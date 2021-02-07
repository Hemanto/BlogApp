from django.contrib import admin
from .models import *
from django import forms

class BlogAdminForm(forms.ModelForm):
    class Meta:
        model = Blog
        widgets = {
            'category': CheckboxSelectMultiple(),
            'subcategory': CheckboxSelectMultiple(),
        }
        fields = '__all__'

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm


admin.site.register(Category)

class SubcategoryAdminForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        widgets = {
            'category': CheckboxSelectMultiple(),
        }
        fields = '__all__'

@admin.register(SubCategory)
class SubcategoryAdmin(admin.ModelAdmin):
    form = SubcategoryAdminForm

