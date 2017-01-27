from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from .models import Base, Word, SubWord

class TitleView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super(TitleView, self).get_context_data(**kwargs)
        context['symbols'] = Base.objects.all()
        return context

class SubWordsView(TemplateView):
    template_name = 'subwords.html'

    def get_context_data(self, **kwargs):
        context = super(SubWordsView, self).get_context_data(**kwargs)
        context['word'] = get_object_or_404(Word, id=kwargs['id'])
        context['subwords'] = SubWord.objects.filter(ext_of = context['word'])
        return context

class LevelView(TemplateView):
    template_name = 'subwords.html'

    def get_context_data(self, **kwargs):
        context = super(LevelView, self).get_context_data(**kwargs)
        context['subwords'] = SubWord.objects.filter(level=kwargs['level'])
        return context


# Create your views here.
