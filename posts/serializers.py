from rest_framework import serializers
import json
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    Simple serializer that list all posts API with all fields
    """

    # Method to change post.comments return, will return a list with json comments - [{"text": "comment"}]
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_comments(self, obj):
        return json.loads(obj.comments)
