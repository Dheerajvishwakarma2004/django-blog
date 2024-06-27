from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Post 
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'object_list'

class BlogDetail(DetailView):
    model = Post
    template_name = 'blogdetail.html'

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
        else:
            print(form.errors) 
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})
