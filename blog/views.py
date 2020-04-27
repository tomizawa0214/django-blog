from django.utils import timezone
from blog.models import Post
from blog.forms import PostForm
from django.views.generic import (ListView, DetailView, CreateView, UpdateView)

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"

    def get_queryset(self):
        return Post.objects.all()
        # 後でこちらに変更
        # return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

class CreatePostView(CreateView):
    template_name = "blog/post_form.html"
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class PostUpdateView(UpdateView):
    template_name = "blog/post_form.html"
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post