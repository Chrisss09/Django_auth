from django.contrib import admin
from django.urls import path
from accounts.views import index, logout, login, register, user_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('accounts/logout/', logout, name='logout'),
    path('accounts/login/', login, name='login'),
    path('accounts/register/', register, name='register'),
    path('accounts/profile/', user_profile, name='profile'),
]
