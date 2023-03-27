from django.shortcuts import render, redirect
from .models import Music, Playlist

def home(request):
    if request.method == 'GET':
        search_music = request.GET.get('search-music')
        data = {'search': '' if search_music == None else search_music}
        
        musics_name = Music.objects.filter(name__icontains=data['search'])
        musics_artist = Music.objects.filter(artist__icontains=data['search'])
        musics = musics_name.union(musics_artist)

        if musics == '':
            data['musics'] = Music.objects.all()
        data['musics'] = musics
        
        playlist = Playlist.objects.first().musics.all()
        data['playlist'] = playlist

        print(data)
    
    return render(request, 'pages/index.html', data)

def add_music(request, id):
    playlist = Playlist.objects.first()
    playlist.musics.add(id)
    playlist.save()

    return redirect('/')

def delete_music(request, id):
    playlist = Playlist.objects.first()
    playlist.musics.remove(id)
    playlist.save()

    return redirect('/')