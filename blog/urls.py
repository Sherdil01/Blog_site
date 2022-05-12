from django.urls import path
from .views import *
urlpatterns = [
    path('', BlogList.as_view(), name='blog_list'),
    path('category/<slug:slug>', BlogByCategory.as_view(), name='category_blogs'),
    path('create/', BlogCreate.as_view(), name='blog_create'),
    path('tag/<slug:slug>', BlogByTag.as_view(), name='tag_blogs'),
    path('blog/<slug:slug>', BlogDetail.as_view(), name='blog_detail'),
    path('comment-delete/<int:pk>', CommentDelete.as_view(), name='comment_delete'),
    path('category-list', CategoryList.as_view(), name='category_list'),
    path('category-user/<slug:slug>', CategoryAddUser.as_view(), name='category_user_add'),
    path('blog-update/<slug:slug>', BlogUpdate.as_view(), name='blog_update'),
    path('about/', AboutList.as_view(), name='about_list')
    
]





