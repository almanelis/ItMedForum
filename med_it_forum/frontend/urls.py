from django.urls import path
from . import views

app_name = 'frontend'

urlpatterns = [
    path('main_page/', views.MainPageView.as_view()),
    path('profile_page/', views.ProfilePageView.as_view()),
    path('other/', views.OtherView.as_view()),
]
