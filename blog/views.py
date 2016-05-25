from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from . models import Post
from . forms import Postform

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('-published_date')
    return render(request, 'blog/index.html', {'posts':posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_about(request):
    return render(request, 'blog/about.html')

def AHP_survey(request):
    return render(request, 'blog/ahp_survey.html')

# @login_required
def post_new(request):
    if request.method == 'POST':
        form = Postform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date=timezone.now()
            post.save()
            return redirect('blog.views.post_detail',pk=post.pk)
    else:
        form = Postform()
    return render(request, 'blog/post_edit.html',{'form':form})

def post_edit(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = Postform(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date=timezone.now()
            post.save()
            return redirect('blog.views.post_detail',pk=post.pk)
    else:
        form = Postform(instance=post)
    return render(request, 'blog/post_edit.html',{'form':form})

def post_delete(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog.views.post_list')

def sign_up(request):
    if request.method == "POST":
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            userform.save()
            return redirect('blog.views.signup_ok')
    elif request.method == "GET":
        userform = UserCreationForm()
    return render(request, "registration/signup.html", {
        "userform": userform,
        })
def signup_ok(request):
    return render(request, "registration/signup_ok.html")
