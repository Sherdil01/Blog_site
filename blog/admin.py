
from django.contrib import admin
from .models import Category, Blog, Tag, Comment

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    prepopuladsadted_fields = {'slug': ('name',)}
    
@admin.register(Comment)
class TagAdmin(admin.ModelAdmin):
    list_display = ['text']
    
    
    
# Register your models here.
