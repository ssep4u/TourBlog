from django.views.generic import CreateView
from .models import Post
from .forms import PostForm

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm


post_new = PostCreateView.as_view()


