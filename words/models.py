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


# Create your models here.
