from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import UserRegisterForm, PostForm
from django.contrib import messages
from .services import *
from django.contrib.auth.models import User
import random

# Create your views here.
def feed(request):
    posts = Post.objects.all()
    #rival = User.objects.order_by('?').first().username

    

    context = {'posts': posts}

    return render(request, 'pokemon/feed.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'¡Usuario {username} creado con exito!')
            return redirect('feed')
    else:
        form = UserRegisterForm()

    context = { 'form' : form }
    return render(request, 'pokemon/register.html', context)    

def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk)

    #prev = random.randint(0,1)
    #if prev == 1:
    #    resultado = Post.objects(resultado='¡Victoria!')
    #else:
    #    resultado = Post.objects(resultado='¡Derrota!')

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Batalla Finalizada!')
            return redirect('feed')
    else:
        form = PostForm()

    return render(request, 'pokemon/batalla.html', {'form': form})

def profile(request, username=None):
    current_user = request.user

    if username and username != current_user.username:
        user = User.objects.get(username=username)
        posts = user.posts.all()
    else:
        posts = current_user.posts.all()
        user = current_user
    return render(request, 'pokemon/profile.html', {'user': user, 'posts': posts})


