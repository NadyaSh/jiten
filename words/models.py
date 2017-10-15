from django.db import models
from django.core.urlresolvers import reverse

class Base(models.Model):
    word_jap = models.CharField(max_length=300)
    img_offset = models.IntegerField()

    def __str__(self):
        return self.word_jap

class Word(models.Model):
    word_jap = models.CharField(max_length=300)
    ext_of = models.ForeignKey(Base, related_name='words')

    def __str__(self):
        return self.word_jap

    def get_absolute_url(self):
        return reverse('subwords', kwargs={'id': self.id})

class SubWord(models.Model):
    word_jap = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    level = models.IntegerField()
    ext_of = models.ForeignKey(Word, related_name='subs')

    def __str__(self):
        return self.word_jap

class Kanji(models.Model):
    name = models.CharField(max_length=5, default='')
    level = models.IntegerField()
    file_name = models.CharField(max_length=300)
    onYomi = models.CharField(max_length=300, blank=True)
    kunYomi = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_url(self):
        return 'img/kanji/%s/%s.gif' % (self.level, self.file_name)

    def get_static_url(self):
        return 'img/kanji/%s_static/%s_still.gif' % (self.level, self.file_name)

    def get_absolute_url(self):
        return reverse('kanji', kwargs={'id': self.id})

    def get_absolute_url2(self):
        return reverse('kanji2', kwargs={'name': self.name})

# Create your models here.
