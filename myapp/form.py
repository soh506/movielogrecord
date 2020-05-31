from django.forms import ModelForm, inlineformset_factory
from myapp.models import Movie, Director, Log

class DirectorForm(ModelForm):
    class Meta:
        model = Director
        fields = ('name',)

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ('title','watch_date', 'director')

class LogForm(ModelForm):
    class Meta:
        model = Log
        fields = ('movie','text')



'''
MovieFormset = inlineformset_factory(
    parent_model=Director,
    model=Movie,
    form=MovieForm,
    can_delete=False,
    extra=1,
)

LogFormset = inlineformset_factory(
    parent_model= Movie,
    model=Log,
    form=LogForm,
    can_delete=False,
    extra=1,
)
'''