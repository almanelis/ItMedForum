from django.conf import settings
from django.views.generic.edit import CreateView

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, reverse_lazy

from users.forms import CustomUserCreationForm

urlpatterns = [
    # Лента с статьями
    path('', include('feed.urls')),
    # Приложение для работы с пользователями
    path('auth/', include('django.contrib.auth.urls')),
    # Регистрация пользователя
    path(
    'auth/registration/', 
    CreateView.as_view(
        template_name='registration/registration_form.html',
        form_class=CustomUserCreationForm,
        success_url=reverse_lazy('feed:list'),
    ),
    name='registration',
    ),
    # Профиль пользователя
    path('users/', include('users.urls'), name='users'),
    # Приложение админки
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
