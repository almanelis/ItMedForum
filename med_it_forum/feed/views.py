from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from .forms import PostForm
from .models import Post


class PostListView(ListView):
    """Функция вывода списка постов в ленте"""
    model = Post
    context_object_name = 'posts'
    template_name = 'feed/post_list.html'
    # Фильтрация от нового к старому
    ordering = ['-created_at',]


class PostCreateView(LoginRequiredMixin, CreateView):
    """Функция создания поста на основе модели и формы поста"""
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('feed:list')
    
    # Функция для автоматического назначения автора поста
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    template_name='feed/post_detail.html'