from django.urls import path, include
from myapp import views

app_name = 'myapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('movie/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('register/director/', views.RegisterDirectorView.as_view(), name='registerdirector'),
    path('register/movie/', views.RegisterMovieView.as_view(), name='registermovie'),
    path('writing/log/', views.WritingLogView.as_view(), name='writinglog'),
    path('writing/thismovie/<int:movie_id>/log/', views.writingthismovielog, name='writingthismovielog'),
    path('update/log/<int:pk>/', views.UpdateLogView.as_view(), name='updatelog'),
    path('delete/log/<int:pk>/', views.DeleteLogView.as_view(), name='deletelog'),
    path('delete/movie/<int:pk>/', views.DeleteMovieView.as_view(), name='deletemovie'),
]