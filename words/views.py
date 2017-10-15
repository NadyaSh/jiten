import os
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404
from .models import Word, SubWord, Kanji
from django.db.models import Count
from django.http import JsonResponse

class TitleView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super(TitleView, self).get_context_data(**kwargs)
        all_subs = SubWord.objects.all()
        counts = [0 for i in range(1, 6)]
        for sw in all_subs:
            counts[sw.level - 1] += 1
        context['count_by_level'] = [{'level': str(i), 'count': counts[i - 1]} for i in range(1, 6)]
        context['section'] = 'jiten'
        context['words'] = Word.objects.all().order_by('ext_of__word_jap').order_by('word_jap').distinct().annotate(num_subs=Count('subs')).select_related('ext_of')
        return context

class SubWordsView(TemplateView):
    template_name = 'subwords.html'

    def get_context_data(self, **kwargs):
        level = self.request.GET.get("level", -1)
        word_id = self.request.GET.get("id", -1)
        context = super(SubWordsView, self).get_context_data(**kwargs)
        context['word'] = get_object_or_404(Word, id=word_id)
        context['section'] = 'jiten'
        if level != -1:
            context['subwords'] = SubWord.objects.filter(ext_of = context['word']).filter(level=level).select_related('ext_of')
        else:
            context['subwords'] = SubWord.objects.filter(ext_of = context['word']).select_related('ext_of')
        return context

class LevelView(TemplateView):
    template_name = 'by_level.html'

    def get_context_data(self, **kwargs):
        context = super(LevelView, self).get_context_data(**kwargs)

        all_subs = SubWord.objects.all()
        counts = [0 for i in range(1, 6)]
        for sw in all_subs:
            counts[sw.level - 1] += 1
        context['count_by_level'] = [{'level': str(i), 'count': counts[i - 1]} for i in range(1, 6)]

        context['level'] = kwargs['level']
        context['section'] = 'jiten'
        context['words'] = Word.objects.filter(subs__level=kwargs['level']).order_by('ext_of__word_jap').order_by('word_jap').distinct().select_related('ext_of')
        return context

class KanjiByLevel(TemplateView):
    template_name = 'kanji_by_level.html'

    def get_context_data(self, **kwargs):
        context = super(KanjiByLevel, self).get_context_data(**kwargs)
        all_kanji = Kanji.objects.all()
        counts = [0 for i in range(1,6)]
        for kj in all_kanji:
            counts[kj.level - 1] += 1
        context['count_by_level'] = [{'level': str(i) , 'count':counts[i-1]} for i in range (1,6)]

        context['level'] = kwargs['level']
        context['section'] = 'kanji'
        try:
            context['kanjis'] = Kanji.objects.filter(level=kwargs['level']).order_by('file_name')
        except:
            pass
        return context

class KanjiDetail(TemplateView):
    template_name = 'kanji_detail.html'

    def get_context_data(self, **kwargs):
        context = super(KanjiDetail, self).get_context_data(**kwargs)
        context['section'] = 'kanji'
        context['kanji'] = get_object_or_404(Kanji, id=kwargs['id'])
        return context

class KanjiDetail2(TemplateView):
    template_name = 'kanji_detail.html'

    def get_context_data(self, **kwargs):
        context = super(KanjiDetail2, self).get_context_data(**kwargs)
        context['section'] = 'kanji'
        context['kanji'] = get_object_or_404(Kanji, file_name=kwargs['name'])
        return context

def get_kanji_data(request):
    folder = './words/static/img/kanji/3_static/'
    for filename in os.listdir(folder):
        kanji = Kanji(name=filename[:4], level=3, file_name=filename[:4])
        kanji.save()
        print(filename[:4])
    return JsonResponse({})   
# Create your views here.
