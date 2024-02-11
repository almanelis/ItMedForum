from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

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


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    
    # Ограничиваем доступ для редактирования поста для всех, кроме автора
    def dispatch(self, request, *args, **kwargs):
        get_object_or_404(Post, pk=kwargs['pk'], author=request.user)
        return super().dispatch(request, *args, **kwargs)
    
    # Изменяем время последнего редатирования поста
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.update_at = timezone.now()
        self.object.save()
        return super().form_valid(form)

    # После редактирования переводим пользователя на страницу с детализацией поста
    def get_success_url(self):
        return reverse_lazy('feed:detail', kwargs={'pk': self.object.pk})
    

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('users:profile')

    # Ограничиваем доступ на удаление поста для всех, кроме автора
    def dispatch(self, request, *args, **kwargs):
        get_object_or_404(Post, pk=kwargs['pk'], user=request.author)
        return super().dispatch(request, *args, **kwargs)

    # Функция удаления поста
    # После удаления мы переходим на страницу success_url
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return HttpResponseRedirect(self.success_url)