from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from .models import Base, Word, SubWord
from django.db.models import Count

class TitleView(TemplateView):
    template_name = 'main.html'



    def get_context_data(self, **kwargs):
        context = super(TitleView, self).get_context_data(**kwargs)
        context['count_by_level'] = [{'level': str(i), 'count': len(SubWord.objects.filter(level=i))} for i in
                                     range(1, 6)]
        context['words'] = Word.objects.all().order_by('ext_of__word_jap').order_by('word_jap').distinct().annotate(num_subs=Count('subs')).select_related('ext_of')
        #context['symbols'] = Base.objects.all().order_by('word_jap')
        return context

class SubWordsView(TemplateView):
    template_name = 'subwords.html'

    def get_context_data(self, **kwargs):
        context = super(SubWordsView, self).get_context_data(**kwargs)
        context['l_1'] = len(SubWord.objects.filter(level=1)) > 0
        context['l_2'] = len(SubWord.objects.filter(level=2)) > 0
        context['l_3'] = len(SubWord.objects.filter(level=3)) > 0
        context['l_4'] = len(SubWord.objects.filter(level=4)) > 0
        context['l_5'] = len(SubWord.objects.filter(level=5)) > 0
        context['word'] = get_object_or_404(Word, id=kwargs['id'])
        context['subwords'] = SubWord.objects.filter(ext_of = context['word']).select_related('ext_of')
        return context

class LevelView(TemplateView):
    template_name = 'by_level.html'

    def get_context_data(self, **kwargs):
        context = super(LevelView, self).get_context_data(**kwargs)
        context['count_by_level'] = [{'level': str(i) , 'count':len(SubWord.objects.filter(level=i))} for i in range (1,6)]
        context['level'] = kwargs['level']
        context['words'] = Word.objects.filter(subs__level=kwargs['level']).order_by('ext_of__word_jap').order_by('word_jap').distinct().select_related('ext_of')
        return context


# Create your views here.
