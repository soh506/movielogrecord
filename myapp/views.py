from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic
from myapp.models import Movie, Director, Log
from myapp.form import DirectorForm, MovieForm, LogForm



'''
class IndexView(generic.ListView):
    template_name = 'myapp/index.html'
    context_object_name = 'movie_list'
    queryset = Movie.objects.all()
'''

def index(request):
    movie_list = Movie.objects.all()
    return render(request, 'myapp/index.html', {'movie_list': movie_list})

'''
class MovieDetailView(generic.DetailView):
    model = Movie
    template_name = 'myapp/detail.html'
'''

def moviedetail(request, pk):
    m = Movie.objects.get(pk=pk)
    return render(request, 'myapp/detail.html', {'movie': m})

'''
class RegisterDirectorView(generic.CreateView):
    model = Director
    form_class = DirectorForm
    template_name = 'myapp/register.html'
    def get_success_url(self):
        return reverse('myapp:registermovie') 

'''

def registerdirector(request):
    if request.method == "POST":
        form = DirectorForm(request.POST)
        if form.is_valid():
            d = form.save(commit=False)
            d.save()
            return redirect('myapp:registermovie')
    else:
        form = DirectorForm()
        return render(request, 'myapp/register.html', {'form': form})

'''
class RegisterMovieView(generic.CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'myapp/register.html'
    def get_success_url(self):
        return reverse('myapp:movie_detail', kwargs={'pk': self.object.pk }) 
'''

def registermovie(request):
    if request.method  == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            m = form.save(commit=False)
            m.save()
            return redirect('myapp:movie_detail', pk=m.pk)
    else:
        form = MovieForm()
        return render(request, 'myapp/register.html', {'form': form})

'''
class WritingLogView(generic.CreateView):
    model = Log
    form_class = LogForm
    template_name = 'myapp/register.html'
    def get_success_url(self):
        return reverse('myapp:movie_detail', kwargs={'pk': self.object.movie.pk }) 
'''     

def writinglog(request):
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            l = form.save(commit=False)
            l.save()
            return redirect('myapp:movie_detail', pk=l.movie.pk)
    else:
        form = LogForm()
        return render(request, 'myapp/register.html', {'form': form})

def writingthismovielog(request, movie_id):
    obj = get_object_or_404(Movie, id=movie_id)
    form = LogForm({'movie':obj})
    if request.method == "POST":
        form = LogForm(request.POST)
        if form.is_valid():
            l = form.save(commit=False)
            l.save()
            return redirect('myapp:movie_detail', pk=l.movie.pk)
    else:
        return render(request, 'myapp/register.html', {'form': form})


'''

class UpdateLogView(generic.UpdateView):
    model = Log
    form_class = LogForm
    template_name = "myapp/register.html"
    def get_success_url(self):
        return reverse('myapp:movie_detail', kwargs={'pk': self.object.movie.pk })

'''
def updatelog(request, pk):
    obj = get_object_or_404(Log, id=pk)
    if request.method == "POST":
        form = LogForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('myapp:movie_detail', pk=obj.movie.pk)
    else:
        form = LogForm(instance=obj)
        return render(request, 'myapp/register.html', {'form': form})

'''

class DeleteLogView(generic.DeleteView):
    model = Log
    def get_success_url(self):
        return reverse('myapp:movie_detail', kwargs={'pk': self.object.movie.pk })

'''
def deletelog(request, pk):
    obj = get_object_or_404(Log, id=pk)
    movie_id = obj.movie.pk
    if request.method =="POST": 
        obj.delete() 
        return redirect('myapp:movie_detail', pk=movie_id)
    context = {'obj':obj}
    return render(request, "myapp/delete.html", context)
'''

class DeleteMovieView(generic.DeleteView):
    model = Movie
    def get_success_url(self):
        return reverse('myapp:index')

'''
def deletemovie(request, pk):
    obj = get_object_or_404(Movie, id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('myapp:index')
    context = {'obj':obj}
    return render(request, "myapp/delete.html", context)
