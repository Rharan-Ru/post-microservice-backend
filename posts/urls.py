from django.urls import path

from .views import PostsView, SaveCommentsView

urlpatterns = [
    path('posts', PostsView.as_view(), name='posts_view'),
    path('posts/<str:post_pk>/comments', SaveCommentsView.as_view(), name='save_comments_view'),
]
