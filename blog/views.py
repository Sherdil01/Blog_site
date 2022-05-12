from unicodedata import category
from account.forms import Account
from django import views
from django.shortcuts import redirect, render
from django.views import View
from django.template.defaultfilters import slugify
from blog.forms import BlogForm, CommentForm, BlogUpdateForm
from blog.models import blog, comment
from .models import Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Blog, Category, Tag
from django.views.generic import ListView

class BaseView:
    def category(self):
        category_list = Category.objects.all()
        return category_list
    
    def tag(self):
        tag_list = Tag.objects.all()
        return tag_list
    
    

class BlogList(View, BaseView):
    def get(self, request):
        context = {}
        search = request.GET.get('search')
        if search:
            context['blogs'] = Blog.objects.filter(
                Q(title__icontains=search) | Q(category__name__icontains=search)
                )
        else:
            context['blogs'] = Blog.objects.all()
        context['categories'] = self.category()
        context['tags'] = self.tag()
        return render(request, 'blog/blog_list.html', context)
    


class BlogByCategory(BaseView, View):
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        blogs = Blog.objects.filter(category=category)
        categories = self.category()
        tags = self.tag()
        
        context = {
            'category': category,
            'blogs': blogs,
            'categories': categories,
            'tags': tags
        }
        return render(request, 'blog/category_blogs.html', context)
class BlogByTag(View, BaseView):
    def get(self, request, slug):
        tag = Tag.objects.get(slug=slug)
        blogs = Blog.objects.filter(tags=tag)
        categories = self.category()
        tags = self.tag()
        
        context = {
            'tag': tag,
            'blogs': blogs,
            'categories': categories,
            'tags': tags
        }
        return render(request, 'blog/tag_blogs.html', context)
        
class BlogCreate(LoginRequiredMixin, BaseView, View):
    login_url = reverse_lazy('login')
    def get(self, request):
        context = {}
        context['form'] = BlogForm
        context['categories'] = self.category()
        context['tags'] = self.tag()
        return render(request, 'blog/blog_create.html', context)
    
    def post(self, request):
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form2 = form.save(commit=False) 
            form2.slug = slugify(form2.title)
            form2.user = request.user
            form2.save()
            blog = Blog.objects.get(id=form2.id)
            tags = form.cleaned_data.get('tags')
            tag_list = list(tags.split(','))
            for tag in tag_list:
                tag, create = Tag.objects.get_or_create(name=tag.strip())
                blog.tags.add(tag)
                
            return redirect('blog_list')


class BlogDetail(BaseView,View):
    def get(self, request, slug):
        context = {}
        blog = Blog.objects.get(slug=slug)
        context['blog'] = blog
        context['categories'] = self.category()
        context['tags'] = self.tag()
        context['form'] = CommentForm()
        
        blog.views+=1
        blog.save()
        
        return render(request, 'blog/blog_detail.html', context)
    
    
    def post(self, request, slug):
        form = CommentForm(request.POST)
        if form.is_valid():
            form_comment = form.save(commit=False)
            form_comment.blog = Blog.objects.get(slug=slug)
            form_comment.user = request.user
            form_comment.save()
            return redirect('blog_detail', form_comment.blog.slug)
        
class CommentDelete(View):
    def post(self, request, **kwargs):
        pk = kwargs['pk']
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return redirect('blog_detail', comment.blog.slug)
    


class CategoryList(View, BaseView):
    def get(self, request):
        context = {}
        context['categories'] = self.category()
        context['tags'] = self.tag()        
        
        return render(request, 'blog/category_list.html', context)

class CategoryAddUser(View):
    def get(self, request, slug):
        category = Category.objects.get(slug=slug)
        user = Account.objects.get(username = request.user.username)
        if user in category.user.all():
            category.user.remove(user)
            return redirect('category_list')
        else:
            category.user.add(user)
            return redirect('category_list')
        

class BlogUpdate(View):
    def get(self, request, slug):
        blog = Blog.objects.get(slug=slug)
        tags_value = ''
        for tag in blog.tags.all():
            tags_value +=str(tag)
            tags_value +=','
        
        form = BlogUpdateForm(instance=blog)
        context = {
            'blog': blog,
            'form': form,
            'tags_value': tags_value
        }
        return render(request, 'blog/blog_update.html', context)
    
    def post(self, request, slug):
        blog = Blog.objects.get(slug=slug)
        form = BlogUpdateForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form_create = form.save(commit=False)
            form_create.slug = slugify(form_create.title)
            form_create.user = request.user
            form_create.save()
            tags = request.POST['tags'].split(',')
            for tag in blog.tags.all():
                if tag not in tags:
                    blog.tags.remove(tag)
            for tag in tags:
                if tag!='':
                    tag, created = Tag.objects.get_or_create(name=tag.strip())
                    blog.tags.add(tag)
            return redirect('blog_list')
        

class AboutList(ListView):
    template_name = 'blog/about.html'