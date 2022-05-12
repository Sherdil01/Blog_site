from unicodedata import category
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from blog.views import BaseView
from django.contrib import messages
from .forms import ProfileUpdateForm
from django.db.models import Q



from .forms import RegisterForm
from .models import Account

class LoginView(View, BaseView):
    def get(self, request):
        context = {}
        context['categories'] = self.category()
        context['tags'] = self.tag()
        return render(request, 'account/login.html', context)
       
    
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('pass')
        
        user = authenticate(username=username, password=password)
    
        if user is not None:
            login(request, user)  
            return redirect('blog_list')
        else:
            messages.info(request, 'username yoki password xato kiritilgan!!!')
            return redirect('login')
        

class RegisterForm(CreateView, BaseView):
    model = Account
    form_class = RegisterForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')
    
    def get_context_data(self, **kwargs,):
        context = super().get_context_data(**kwargs)
        context['categories'] = self.category()
        context['tags'] = self.tag()
        return context
    


class Userprofile(View, BaseView):
    def get(self, request):
        username = request.user.username
        profile = Account.objects.get(username=username)
        context = {
            'profile': profile,
            'categories': self.category(),
            'tags': self.tag()
        }
        
        
        return render(request, 'account/profile.html', context)
    
    
    
class UserUpdate(UpdateView, BaseView):
    model = Account
    form_class = ProfileUpdateForm
    template_name = 'account/user_update.html'
    success_url = reverse_lazy('profile')
    
    
    def get_context_data(self, **kwargs):
        context = super(UserUpdate, self).get_context_data()
        context['categories'] = self.category()
        context['tags'] = self.tag()
        return context

class UserList(View, BaseView):
    def get(self, request):
        username = request.GET.get('search')
        if username:
            users = Account.objects.filter(Q(username__icontains=username) | Q(phone_number__icontains=username) | Q(email__icontains=username))
        else:
            users = Account.objects.all()
 
        context = {
        'users': users,
        'categories': self.category,
        'tags': self.tag
    }
        return render(request, 'account/user_list.html', context)