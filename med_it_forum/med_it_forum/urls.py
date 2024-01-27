from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

from django.contrib import admin
from django.urls import include, path, reverse_lazy

from users.forms import CustomUserCreationForm

urlpatterns = [
    # Основне приложения
    path('', include('feed.urls')), # лента

    # Приложение для работы с пользователями
    path('auth/', include('django.contrib.auth.urls')),
    # Регистрация пользователя
    path(
    'auth/registration/', 
    CreateView.as_view(
        template_name='registration/registration_form.html',
        form_class=CustomUserCreationForm,
        success_url=reverse_lazy('feed:index'),
    ),
    name='registration',
    ),

    # Приложение админки
    path('admin/', admin.site.urls),
]
