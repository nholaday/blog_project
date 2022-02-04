"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogapp import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<str:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<str:pk>/edit', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<str:pk>/remove', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<str:pk>/publish', views.post_publish, name='post_publish'),
    path('post/drafts/', views.DraftListView.as_view(), name='post_draft_list'),
    path('post/<str:pk>/comment', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<str:pk>/approve', views.comment_approve, name='comment_approve'),
    path('comment/<str:pk>/remove', views.comment_remove, name='comment_remove'),
]
