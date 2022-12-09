from django.urls import path
from . import views

app_name = 'anime'

urlpatterns = [
    path('', views.index, name='index'),
    path('anime/', views.AnimeListView.as_view(), name='anime_list'),
    path('anime/<int:pk>/', views.AnimeDetailView.as_view(), name='anime_info'),
    path('anime/create/', views.AnimeCreateView.as_view(), name='create_anime'),
    path('anime/<int:pk>/update/', views.AnimeUpdateView.as_view(), name='update_anime'),
    path('director/<int:pk>/', views.DirectorDetailView.as_view(), name='director_info'),
    path('director/create/', views.DirectorCreateView.as_view(), name='create_director'),
    path('director/<int:pk>/update/', views.DirectorUpdateView.as_view(), name='update_director'),
    path('anime/<int:anime_id>/add_to_my_list/<int:user_id>/', views.AddToMyList, name='add_to_my_list'),
    path('anime/<int:anime_id>/delete_from_my_list/<int:user_id>/', views.DeleteFromMyList, name='delete_from_my_list'),
    path('anime/mylist', views.mylist, name='mylist'),
    path('studio/<int:pk>/', views.StudioDetailView.as_view(), name='studio_info'),
    path('studio/create/', views.StudioCreateView.as_view(), name='create_studio'),
    path('studio/<int:pk>/update/', views.StudioUpdateView.as_view(), name='update_studio'),
    path('anime/all', views.AnimeAllListView.as_view(), name='all_anime'),
]