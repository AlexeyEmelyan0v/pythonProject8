from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from django.contrib.auth.models import User, Permission
from django.contrib import messages

from .models import Anime, Director, Studio
from django.template import loader

def index(request) :
    return render(request, 'home.html')

class StudioDetailView(DetailView):
    model = Studio
    template_name = 'anime/studio_detail.html'

class StudioUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'anime.change_studio'
    model = Studio
    fields = ['name']

class StudioCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'anime.add_studio'
    model = Studio
    fields = ['name']

class DirectorDetailView(DetailView):
    model = Director
    template_name = 'anime/director_detail.html'

class DirectorCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'anime.add_director'
    model = Director
    fields = ['name', 'birth_date', 'image']

class DirectorUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'anime.change_director'
    model = Director
    fields = ['name', 'birth_date', 'image']

class AnimeDetailView(DetailView):
    model = Anime
    template_name = 'anime/anime_detail.html'

class AnimeCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'anime.add_anime'
    model = Anime
    fields = ['title', 'director', 'studio', 'release_date', 'image', 'description', 'link']

class AnimeUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'anime.change_anime'
    model = Anime
    fields = ['title', 'director', 'studio', 'release_date', 'image', 'description', 'link']

class AnimeListView(ListView):
    model = Anime
    template_name = 'anime/index.html'
    paginate_by = 5

    def get_ordering(self):
        return 'title'

class AnimeAllListView(ListView):
    model = Anime
    template_name = 'anime/anime_all.html'

    def get_ordering(self):
        return 'title'

def AddToMyList(request, anime_id, user_id):
    user = User.objects.get(id=user_id)
    anime = Anime.objects.get(id=anime_id)
    anime.viewers.add(user)
    anime.save()
    return render(request, 'anime/add_to_my_list.html', {'anime' : anime})

def DeleteFromMyList(request, anime_id, user_id):
    user = User.objects.get(id=user_id)
    anime = Anime.objects.get(id=anime_id)
    anime.viewers.remove(user)
    return render(request, 'anime/delete_from_my_list.html', {'anime' : anime})

def mylist(request):
    return render(request, 'anime/mylist.html')


# Create your views here.