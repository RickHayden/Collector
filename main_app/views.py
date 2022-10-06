from django.shortcuts import render, redirect
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
from .models import Artist, Song, Playlist
# This will import the class we are extending 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = "home.html"
    # Here we have added the playlists as context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["playlists"] = Playlist.objects.all()
        return context



class About(TemplateView):
    template_name = 'about.html'

    # Here we are adding a method that will be run when we are dealing with a GET request
    # def get(self, request):
        # Here we are returning a generic response
        # This is similar to response.send() in express
        # return HttpResponse("About Us")
 #adds artist class for mock database data


# below comments are adding the artist string, we have now updated it to take artists from our database
# class Artist:
#     def __init__(self, name, image, bio):
#         self.name = name
#         self.image = image
#         self.bio = bio


artists = [
  Artist("Gorillaz", "https://i.scdn.co/image/ab67616d00001e0295cf976d9ab7320469a00a29",
          "Gorillaz are once again disrupting the paradigm and breaking convention in their round the back door fashion with Song Machine, the newest concept from one of the most inventive bands around."),
  Artist("Panic! At The Disco",
          "https://i.scdn.co/image/58518a04cdd1f20a24cf0545838f3a7b775f8080", "Welcome 👋 The Amazing Beebo was working on a new bio but now he's too busy taking over the world."),
  Artist("Joji", "https://i.scdn.co/image/7bc3bb57c6977b18d8afe7d02adaeed4c31810df",
          "Joji is one of the most enthralling artists of the digital age. New album Nectar arrives as an eagerly anticipated follow-up to Joji's RIAA Gold-certified first full-length album BALLADS 1, which topped the Billboard R&B / Hip-Hop Charts and has amassed 3.6B+ streams to date."),
  Artist("Metallica",
          "https://i.scdn.co/image/ab67706c0000da84eb6bb372a485d26fd32d1922", "Metallica formed in 1981 by drummer Lars Ulrich and guitarist and vocalist James Hetfield and has become one of the most influential and commercially successful rock bands in history, having sold 110 million albums worldwide while playing to millions of fans on literally all seven continents."),
  Artist("Bad Bunny",
          "data:image/jpeg;base64,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", "Benito Antonio Martínez Ocasio, known by his stage name Bad Bunny, is a Puerto Rican rapper, singer, and songwriter. His music is often defined as Latin trap and reggaeton, but he has incorporated various other genres into his music, including rock, bachata, and soul"),
  Artist("Kaskade",
          "https://i1.sndcdn.com/artworks-sNjd3toBZYCG-0-t500x500.jpg", "Ryan Gary Raddon, better known by his stage name Kaskade, is an American DJ, record producer, and remixer."),
  Artist("Coolio",
          "data:image/jpeg;base64,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", "Rest in Peace."),
]

class ArtistList(TemplateView):
    template_name = "artist_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["artists"] = Artist.objects.filter(
                name__icontains=name, user=self.request.user)
            context["header"] = f"Searching for {name}"
        else:
            context["artists"] = Artist.objects.filter(user=self.request.user)
            context["header"] = "Trending Anime"
        return context




class ArtistCreate(CreateView):
    model = Artist
    fields = ['name', 'img', 'bio']
    template_name = "artist_create.html"

    # This is our new method that will add the user into our submitted form
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ArtistCreate, self).form_valid(form)

    def get_success_url(self):
        print(self.kwargs)
        return reverse('artist_detail', kwargs={'pk': self.object.pk})


class ArtistDetail(DetailView):
    model = Artist
    template_name = "artist_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["playlists"] = Playlist.objects.all()
        return context


class ArtistUpdate(UpdateView):
    model = Artist
    fields = ['name', 'img', 'bio', 'verified_artist']
    template_name = "artist_update.html"
    success_url = "/artists/"


    def get_success_url(self):
        return reverse('artist_detail', kwargs={'pk': self.object.pk})

class ArtistDelete(DeleteView):
    model = Artist
    template_name = "artist_delete_confirmation.html"
    success_url = "/artists/"


class SongCreate(View):

    def post(self, request, pk):
        title = request.POST.get("title")
        length = request.POST.get("length")
        artist = Artist.objects.get(pk=pk)
        Song.objects.create(title=title, length=length, artist=artist)
        return redirect('artist_detail', pk=pk)

class PlaylistSongAssoc(View):

    def get(self, request, pk, song_pk):
        # get the query param from the url
        assoc = request.GET.get("assoc")
        if assoc == "remove":
            # get the playlist by the id and
            # remove from the join table the given song_id
            Playlist.objects.get(pk=pk).songs.remove(song_pk)
        if assoc == "add":
            # get the playlist by the id and
            # add to the join table the given song_id
            Playlist.objects.get(pk=pk).songs.add(song_pk)
        return redirect('home')


class Signup(View):
    # show a form to fill out
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    # on form submit, validate the form and login the user.
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("artist_list")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
