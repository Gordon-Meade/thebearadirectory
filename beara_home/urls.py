from django.urls import path, include
from .views import PostList, post_detail, comment_edit, comment_delete, index_view, home_view, posts_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('index/', index_view, name='index'),
    path('home/', home_view, name='home'),
    path('posts/', posts_view, name='posts'),
    path('post/<slug:slug>/', post_detail, name='post-detail'),
    path('post/<slug:slug>/edit_comment/<int:comment_id>/', comment_edit, name='comment-edit'),
    path('post/<slug:slug>/delete_comment/<int:comment_id>/', comment_delete, name='comment-delete'),
    path('logout/', auth_views.LogoutView.as_view(), name='account_logout'),
]
