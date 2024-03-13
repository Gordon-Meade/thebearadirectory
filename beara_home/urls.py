from django.urls import path
from .views import PostList, post_detail, comment_edit, comment_delete, index_view, home_view

urlpatterns = [
    path('index/', index_view, name='index'),
    path('home/', home_view, name='home'),
    path('post/', PostList.as_view(), name='post-list'),
    path('post/<slug:slug>/', post_detail, name='post-detail'),
    path('post/<slug:slug>/edit_comment/<int:comment_id>/', comment_edit, name='comment-edit'),
    path('post/<slug:slug>/delete_comment/<int:comment_id>/', comment_delete, name='comment-delete'),
]
