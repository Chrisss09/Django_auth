from django.contrib import admin
from django.urls import path
from accounts.views import index, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('accounts/logout/', logout, name='logout'),
]
