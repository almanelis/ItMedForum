from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Лента с статьями
    path('', include('feed.urls')),
    # Приложение для работы с пользователями
    path('auth/', include('django.contrib.auth.urls')),
    # Приложение пользователя
    path('users/', include('users.urls'), name='users'),
    # Тестовая вёрстка
    path('frontend/', include('frontend.urls'), name='frontend'),
    # Редактор статей
    path('froala_editor/', include('froala_editor.urls')),
    # Обновление страниц
    path("__reload__/", include("django_browser_reload.urls")),
    # Приложение админки
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
