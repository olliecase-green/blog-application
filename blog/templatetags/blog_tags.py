from django import template
from ..models import Post
from django.db.models import Count

register = template.Library()


@register.simple_tag()
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/additional_posts.html')
def show_most_commented_posts(count=5):
    most_commented_posts = (
        Post
        .published
        .annotate(total_comments=Count('comments'))
        .order_by('-total_comments')[:count]
    )
    return {'additional_posts': most_commented_posts}


@register.inclusion_tag('blog/post/additional_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'additional_posts': latest_posts}
