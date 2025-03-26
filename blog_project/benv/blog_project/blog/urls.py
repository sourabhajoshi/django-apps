from django.urls import path
from .views import *

urlpatterns = [
    path('catagories/', CategoryListCreateView.as_view(), name='category-list'),
    path('posts/', PostListCreateView.as_view(), name="post-list"),
    path('posts/<int:pk>', PostListCreateView.as_view(), name='post-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list'),
    path('posts/<int:post_id>/like/', LikeCreateView.as_view(), name='like-post')
]
