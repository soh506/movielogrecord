from django.urls import path, include
from myapp import views

app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:pk>/', views.moviedetail, name='movie_detail'),
    path('register/director/', views.registerdirector, name='registerdirector'),
    path('register/movie/', views.registermovie, name='registermovie'),
    path('writing/log/', views.writinglog, name='writinglog'),
    path('writing/thismovie/<int:movie_id>/log/', views.writingthismovielog, name='writingthismovielog'),
    path('update/log/<int:pk>/', views.updatelog, name='updatelog'),
    path('delete/log/<int:pk>/', views.deletelog, name='deletelog'),
    path('delete/movie/<int:pk>/', views.deletemovie, name='deletemovie'),
]