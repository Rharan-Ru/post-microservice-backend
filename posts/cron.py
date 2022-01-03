from django.db import connections
from .models import Post
import json


# Syncronize Comments Database with Posts Database if they are differents
def sync_comments():
    comments = get_comments()
    posts = Post.objects.all()

    for post in posts:
        p_comments = json.loads(post.comments)
        filtered_comments = [{"text": c["text"]} for c in comments if c['post_id'] == post.id]
        if len(p_comments) < len(filtered_comments):
            post.comments = json.dumps(filtered_comments)
            post.save()


# Get all comments from comments-microservice-backend database and return organized data
def get_comments():
    with connections['comments_db'].cursor() as cursor:
        cursor.execute('SELECT * FROM comment_comment;')
        collumns = [col[0] for col in cursor.description]

        return [dict(zip(collumns, row)) for row in cursor.fetchall()]
