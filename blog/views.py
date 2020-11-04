from django.shortcuts import render, get_object_or_404
from .models import Post,Comment #Comment Model Import
from .forms import CommentForm

from django.shortcuts import redirect
# Create your views here.
def post_list(request):
    posts = Post.objects.all()

    


    return render(request,
    'blog/list.html',
    {'posts': posts,
    })

def post_detail(request, post):
    post = get_object_or_404(Post, slug=post)

    comments = Comment.objects.filter(post=post) #list of comments

    if request.method == 'POST':
        # A comment was posted
        form = CommentForm(request.POST)
        form.instance.author = request.user
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('/')
    else:
        form = CommentForm()
    
    return render(request,
    'blog/detail.html',
    {'post': post,
    'comments': comments,
    'form': form})