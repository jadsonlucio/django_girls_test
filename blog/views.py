from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse

from .models import Postagem
from .forms import PostForm

# Create your views here.

def home_screen(request):
    postagens_hoje = Postagem.objects.filter(data_publicacao__lte = timezone.now()).order_by("data_publicacao")

    print(postagens_hoje)
    return render(request, "blog/posts.html", {"postagens_hoje" : postagens_hoje})

def show_post(request, id):
    postagem = post = get_object_or_404(Postagem, pk=id)
    print(postagem)
    return render(request, "blog/post.html", {"postagem" : postagem})


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.autor = request.user
            post.data_publicacao = timezone.now()
            post.save()

            return redirect('post_show', id = post.pk)
    else:
        form = PostForm()
    
    return render(request, 'blog/create_posts.html', {'form' : form})