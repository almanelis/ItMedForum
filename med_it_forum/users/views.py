from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from feed.models import Post
from .forms import CustomUserCreationForm, CustomUserUpdateForm


User = get_user_model()


class UserCreateView(CreateView):
    """Фукнция регистрации пользователя"""
    template_name = 'registration/registration_form.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('feed:list')

class UserUpdateView(LoginRequiredMixin, UpdateView):
    """Функция редактирования профиля пользователя"""
    model = User
    form_class = CustomUserUpdateForm
    template_name = 'profile/user_form.html'
    success_url = reverse_lazy('users:profile')
    
    # Ограничиваем доступ для редактирования профиля для всех, кроме его обладателя
    # def dispatch(self, request, *args, **kwargs):
    #     get_object_or_404(User, pk=kwargs['pk'], user=request.user)
    #     return super().dispatch(request, *args, **kwargs)


class UserDetailView(DetailView):
    """Функция просмотра профиля пользователя"""
    model = User
    template_name = 'profile/user_detail.html'
    context_object_name = 'current_user'


def profile(request):
    user = request.user 
    user_posts = Post.objects.filter(author=user)
    context = {
        'user_posts': user_posts,
    }
    template = 'profile/user_profile.html'
    return render(request, template, context)
    
