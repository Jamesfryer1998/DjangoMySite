import sys
import time

from blog.models import Post

def post_on_blog(titles, bodys):

    post = Post(title=titles, body=bodys)
    post.save()

post_on_blog('First Blog', 'testing text')