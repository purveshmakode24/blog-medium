from django.shortcuts import render, redirect
from .models import Post, Like, Dislike
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserRegisterForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# import filters

def home(request):
    if request.method == "POST":   
        auth_name = request.POST.get('author_name')

        if auth_name == 'All (Home)':
            messages.success(request, f'Filter applied for "All"')
            return redirect('blog-home')           
        else:
            #filtering
            filteredPosts =  True

            if auth_name == '':
                return redirect('blog-home')  
            elif User.objects.filter(username = auth_name).exists():
                selectedUser = User.objects.get(username = auth_name)  # returns object
                postsbySelectedUser = selectedUser.myapp_posts.all().order_by('-date_posted')  #returns query set
                messages.success(request, f'Filter applied for "{auth_name}"')
            else:
                selectedUser = None
                postsbySelectedUser = None
                if len(auth_name)>=40:
                    messages.warning(request, f'No results found for your search "{auth_name[:40]}...". Please select relevant option from the filter.')
                else:
                    messages.warning(request, f'No results found for your search "{auth_name}". Please select relevant option from the filter.')
            

            total_users = User.objects.all().count()
            total_posts_count = Post.objects.all().count()

            likes = Like.objects.all()
            dislikes = Dislike.objects.all()

            total_likes = Like.objects.all().count()
            total_dislikes = Dislike.objects.all().count()

            users = User.objects.all()  

            allLikedPostsByCurrentUser = [like.post_id for like in likes if like.liked_user_id == request.user.id]
            allDislikedPostsByCurrentUser = [dislike.post_id for dislike in dislikes if dislike.disliked_user_id == request.user.id] 


            context = {'posts': postsbySelectedUser,
                'total_users': total_users,
                'total_posts_count': total_posts_count,
                'total_likes': total_likes,
                'total_dislikes': total_dislikes,
                'allLikedPostsByCurrentUser': allLikedPostsByCurrentUser,
                'allDislikedPostsByCurrentUser': allDislikedPostsByCurrentUser,
                'users': users,
                'filteredPosts': filteredPosts,
                'selectedUser': selectedUser,
                'unkown_filter_auth': auth_name
                }
            return render(request, "posts.html", context) 
    else:
        total_users = User.objects.all().count()
        posts = Post.objects.all().order_by('-date_posted')
        total_posts_count = Post.objects.all().count()

        likes = Like.objects.all()
        dislikes = Dislike.objects.all()

        total_likes = Like.objects.all().count()
        total_dislikes = Dislike.objects.all().count()

        users = User.objects.all()

        allLikedPostsByCurrentUser = [like.post_id for like in likes if like.liked_user_id == request.user.id]
        allDislikedPostsByCurrentUser = [dislike.post_id for dislike in dislikes if dislike.disliked_user_id == request.user.id] 

        paginator = Paginator(posts, 3)
        page = request.GET.get('page')

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        index = posts.number
        max_index = len(paginator.page_range)
        start_index = index - 3 if index >= 3 else 0
        end_index = index + 3 if index <= max_index - 3 else max_index
        page_range = list(paginator.page_range)[start_index:end_index]   

        context = {'posts': posts,
            'total_users': total_users,
            'total_posts_count': total_posts_count,
            'page_range': page_range,
            'total_likes': total_likes,
            'total_dislikes': total_dislikes,
            'allLikedPostsByCurrentUser': allLikedPostsByCurrentUser,
            'allDislikedPostsByCurrentUser': allDislikedPostsByCurrentUser,
            'users': users
            }
        return render(request, "posts.html", context)
        
         
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            post_email = form.cleaned_data.get('email')
            user = User.objects.filter(email=post_email)
            if user:
                messages.warning(request, f'This email id {post_email} has already been used.')
                return redirect('login')
            else:
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Your Account for {username} has been created Successfully')
                return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'registration/register.html', context)


@login_required
def profile(request, username):
    if request.user.username == username:
        user = User.objects.get(username=request.user)
        user_posts = user.myapp_posts.all()
        user_posts_count = user.myapp_posts.all().count()
       
        likes = Like.objects.all()
        allLikedPostsByCurrentUser = [like.post_id for like in likes if like.liked_user_id == request.user.id]
        allLikedPostsByCurrentUserCount = len(allLikedPostsByCurrentUser)

        return render(request, 'registration/profile.html', {'posts': user_posts, 'user_posts_count': user_posts_count, 'allLikedPostsByCurrentUserCount': allLikedPostsByCurrentUserCount})
    else:
        return render(request, '404.html', {})     


@login_required
def add_posts(request, username):
    return render(request, 'add_posts.html', {})

@login_required
def add_posts_submit(request):
    if request.method == 'POST':
        post_title = request.POST.get('title')
        post_content = request.POST.get('content')
        post_read_min = request.POST.get('read_min')
        post_author_id = request.POST.get('author_id')
        try:
            form = Post(title=post_title, content=post_content, read_min=post_read_min, author_id=post_author_id)
            form.save()
            messages.success(request, f'Post has been successfully added!')
        except Exception as e:
            print(e)
        return redirect('blog-home')    
    else:
        return render(request, '404.html', {})
    


def delete_posts(request, username, pid):
    if request.method == 'POST':
        del_post_of_id = pid
        # resolved deleting of post with same title names, and assign filter to 'post id' instead, as it's always unique
        Post.objects.filter(id=del_post_of_id).delete()
        messages.success(request, f'Your Post has been Deleted!')
        return redirect('profile', username)
    else:
        return render(request, '404.html', {})
    


def update_post(request, username, pid):
    if request.method == 'POST':
        post_id = pid
        update_title_to = request.POST.get('update_title_to')
        update_content_to = request.POST.get('update_content_to')
        Post.objects.filter(id=post_id).update(title=update_title_to, content=update_content_to)
        messages.success(request, f'Your Post has been Updated!')
        return redirect('profile', username)
    else:
        return render(request, '404.html', {})
    


def full_post(request, pid, slug):
    if request.method == 'POST':
        current_post_id = pid
        # getting current post_id from post request so that current post with that id will be shown up on full_post.html
        post = Post.objects.filter(id=current_post_id)
        context = {
            'post': post,
            'current_post_id': current_post_id
        }
        print('post request done')
        return render(request, 'full_post.html', context)
    else:
        current_post_id = pid
        current_post_title_slug = slug

        print("current post_id:", current_post_id)
        print("NO Post request")

        post = Post.objects.filter(id=current_post_id, slug=current_post_title_slug)

        if post:
            context = {
                'post': post,
                'current_post_id': current_post_id
            }
            return render(request, 'full_post.html', context)
        else:
            return render(request, '404.html', {})


@login_required
def like(request, pid, slug):
    if request.method == "POST":
        dislikePostByCurrentUser = Dislike.objects.filter(disliked_user_id = request.user.id, post_id = pid, is_disliked=True)
        likePostByCurrentUser = Like.objects.filter(post_id = pid, liked_user_id=request.user.id, is_liked=True)

        #clicking already clicked liked button
        if likePostByCurrentUser.exists():
            likePostByCurrentUser.delete()
            #updating the post like count in POST model
            post_likes_count = Like.objects.filter(post_id=pid, is_liked=True).count()
            Post.objects.filter(id=pid).update(likes=post_likes_count)
            messages.info(request, f'Removed from Liked posts')
        else:
            try:
                #check if dislike exists before liking, if yes then delete it
                if dislikePostByCurrentUser.exists():
                    dislikePostByCurrentUser.delete()
                    #updating the post dislike count in POST model
                    post_dislikes_count = Dislike.objects.filter(post_id=pid, is_disliked=True).count()
                    Post.objects.filter(id=pid).update(dislikes=post_dislikes_count)

                #liking
                is_liked = True
                like_form = Like(liked_user_id = request.user.id, post_id = pid, is_liked = is_liked)
                like_form.save()
                post_likes_count = Like.objects.filter(post_id=pid, is_liked=True).count()
                Post.objects.filter(id=pid).update(likes=post_likes_count)
                messages.info(request, f'Added to Liked posts!')

            except Exception as e:
                print(e)  
 
        return redirect('blog-home')   
    else:
        return redirect('blog-home') 


@login_required
def dislike(request, pid, slug):
    if request.method == "POST":
        likePostByCurrentUser = Like.objects.filter(liked_user_id = request.user.id, post_id = pid, is_liked=True)
        dislikePostByCurrentUser = Dislike.objects.filter(post_id = pid, disliked_user_id=request.user.id, is_disliked=True)

        #clicking already clicked disliked button
        if dislikePostByCurrentUser.exists():
            dislikePostByCurrentUser.delete()
            #updating the post dislike count in POST model
            post_dislikes_count = Dislike.objects.filter(post_id=pid, is_disliked=True).count()
            Post.objects.filter(id=pid).update(dislikes=post_dislikes_count)
            messages.info(request, f'Dislike removed')
        else:
            try:
                #check if like exists before disliking, if yes then delete it
                if likePostByCurrentUser.exists():
                    Like.objects.filter(liked_user_id = request.user.id, post_id = pid, is_liked=True).delete()
                     #updating the post like count in POST model
                    post_likes_count = Like.objects.filter(post_id=pid, is_liked=True).count()
                    Post.objects.filter(id=pid).update(likes=post_likes_count)

                #disliking
                is_disliked = True
                dislike_form = Dislike(disliked_user_id = request.user.id, post_id = pid, is_disliked = is_disliked)
                dislike_form.save()
                #updating the post dislike count in POST model
                post_dislikes_count = Dislike.objects.filter(post_id=pid, is_disliked=True).count()
                Post.objects.filter(id=pid).update(dislikes=post_dislikes_count)
                messages.info(request, f'You dislike the post')
            except Exception as e:
                print(e)  

        return redirect('blog-home')   
    else:
        return redirect('blog-home')         

@login_required
def my_liked_posts(request, username):
    user = User.objects.get(username=request.user)
    # user_posts = user.myapp_posts.all()
    user_posts_count = user.myapp_posts.all().count()
    all_posts = Post.objects.all().order_by('-date_posted')

    likes = Like.objects.all()
    allLikedPostsByCurrentUser = [like.post_id for like in likes if like.liked_user_id == request.user.id]
    allLikedPostsByCurrentUserCount = len(allLikedPostsByCurrentUser)

    context = {
        'posts': all_posts,
        'user_posts_count': user_posts_count,
        'allLikedPostsByCurrentUser': allLikedPostsByCurrentUser,
        'allLikedPostsByCurrentUserCount': allLikedPostsByCurrentUserCount
    }

    return render(request, 'my_liked_posts.html', context)

 



