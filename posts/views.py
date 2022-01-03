import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Post
from .serializers import PostSerializer
# Create your views here.


class PostsView(APIView):
    """
    Simple Post View API to get all created posts and create new posts, that returns the post and status request
    """
    def get(self, request):
        posts = Post.objects.all().order_by('-id').reverse()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class SaveCommentsView(APIView):
    """
    Save all comments from comments-microservice-backend to respective post
    """
    def post(self, request, post_pk):
        print(request.data)
        post = Post.objects.get(id=post_pk)
        comments = json.loads(post.comments)
        comments.insert(
            0,
            {
                "text": request.data["text"]
            }
        )
        post.comments = json.dumps(comments)
        post.save()
        return Response(status=status.HTTP_200_OK)
