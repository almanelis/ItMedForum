from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    # Регистрация пользователя
    path('registration/', views.UserCreateView.as_view(), name='registration'),
    # Страница профиля пользователя
    path('profile/', views.profile, name='profile'),
    # Редактирование профиля пользователя
    path('<int:pk>/update/', views.UserUpdateView.as_view(), name='update'),
    # Просмотр профиля пользователей
    path('<int:pk>/detail/', views.UserDetailView.as_view(), name='detail'),
]
