from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from .models import Base, Word, SubWord

class TitleView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super(TitleView, self).get_context_data(**kwargs)
        context['words'] = Word.objects.all().order_by('ext_of__word_jap').order_by('word_jap').distinct().select_related('ext_of')
        #context['symbols'] = Base.objects.all().order_by('word_jap')
        return context

class SubWordsView(TemplateView):
    template_name = 'subwords.html'

    def get_context_data(self, **kwargs):
        context = super(SubWordsView, self).get_context_data(**kwargs)
        context['word'] = get_object_or_404(Word, id=kwargs['id'])
        context['subwords'] = SubWord.objects.filter(ext_of = context['word']).select_related('ext_of')
        return context

class LevelView(TemplateView):
    template_name = 'by_level.html'

    def get_context_data(self, **kwargs):
        context = super(LevelView, self).get_context_data(**kwargs)
        context['words'] = Word.objects.filter(subs__level=kwargs['level']).order_by('ext_of__word_jap').order_by('word_jap').distinct().select_related('ext_of')
        return context


# Create your views here.
