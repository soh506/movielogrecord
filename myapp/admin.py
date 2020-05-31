from django.contrib import admin
from myapp.models import Director, Movie, Log

# Register your models here.

admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Log)

