from django.urls import path
from .views import PostList, post_detail, comment_edit, comment_delete
from .views import my_beara_home

urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('<slug:slug>/', post_detail, name='post-detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>/', comment_edit, name='comment-edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>/', comment_delete, name='comment-delete'),
    path('', my_beara_home, name='my_beara_home'),
]
