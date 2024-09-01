from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('contact/', views.contact, name='contact'),
    path('products/<slug>/', views.products, name='products'),
    path('register/', views.register, name='register'),
    path('single/<int:pk>/', views.single, name='single'),
]