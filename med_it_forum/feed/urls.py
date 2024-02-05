from django.urls import path

from . import views

app_name = 'feed'

urlpatterns = [
    # Вывод списка постов
    path('', views.PostListView.as_view(), name='list'),
    # Форма создания поста
    path('create/', views.PostCreateView.as_view(), name='create'),
    # Детальная иформаци о посте
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    # Форма редактирования поста
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='update'),
    # Форма удаления поста
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),
]
