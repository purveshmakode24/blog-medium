from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import filters


# Create your views here.


def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, "posts.html", context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account for {username} has been created Successfully')
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)


@login_required
def profile(request):
    user = User.objects.get(username=request.user)
    user_posts = user.myapp_posts.all()
    # user_posts = UserFilter(request.GET, queryset=posts)
    return render(request, 'registration/profile.html', {'posts': user_posts})


@login_required
def add_posts(request):
    return render(request, 'add_posts.html')


@login_required
def add_posts_submit(request):
    if request.method == 'POST':
        post_title = request.POST.get('title')
        post_content = request.POST.get('content')
        post_author_id = request.POST.get('author_id')
        try:
            form = Post(title=post_title, content=post_content, author_id=post_author_id)
            form.save()
            messages.success(request, f'Post has been Successfully Added!')
        except Exception as e:
            print(e)

    return redirect('blog-home')

# class UserFilter(filters.FieldSet):
#     class Meta:
#         model = Post
#         fields = ['title', 'content', 'date_posted', 'author']
