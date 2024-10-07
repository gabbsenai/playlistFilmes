from django.urls import path
from django.conf.urls.static import static
from setup import settings

from playlist.views import FilmeCreateView, FilmeDeleteView, FilmeDetailView, FilmeListView, FilmeUpdateView, PlaylistCreateView, PlaylistDeleteView, PlaylistDetailView, PlaylistListView, PlaylistUpdateView

urlpatterns = [
    path('', PlaylistListView.as_view(), name='playlist_list'),
    path('create/', PlaylistCreateView.as_view(), name='playlist_create'),
    path('<int:pk>/', PlaylistDetailView.as_view(), name='playlist_detail'),
    path('<int:pk>/edit/', PlaylistUpdateView.as_view(), name='playlist_update'),
    path('<int:pk>/delete/', PlaylistDeleteView.as_view(), name='playlist_delete'),

    path('filme/', FilmeListView.as_view(), name='filme_list'),
    path('filme/<int:pk>/', FilmeDetailView.as_view(), name='filme_detail'),
    path('filme/create/', FilmeCreateView.as_view(), name='filme_create'),
    path('filme/<int:pk>/edit/', FilmeUpdateView.as_view(), name='filme_update'),
    path('filme/<int:pk>/delete/', FilmeDeleteView.as_view(), name='filme_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
