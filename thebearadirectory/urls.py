
from django.contrib import admin
from django.urls import path, include
from beara_home.views import my_beara_home, index_view, posts_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
    path('beara_home/', my_beara_home, name='beara_home'),
    path('', index_view, name='index'),
    path('home/', my_beara_home, name='home'),
    path('posts/', posts_view, name='posts')
]

