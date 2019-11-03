from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse

from .models import Postagem

# Create your views here.

def home_screen(request):
    postagens_hoje = Postagem.objects.filter(data_publicacao__lte = timezone.now()).order_by("data_publicacao")

    print(postagens_hoje)
    return render(request, "blog/posts.html", {"postagens_hoje" : postagens_hoje})