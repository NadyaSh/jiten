from django.contrib import admin
from .models import Base, Word, SubWord, Kanji

admin.site.register(Base)
admin.site.register(Word)
admin.site.register(SubWord)
admin.site.register(Kanji)

# Register your models here.
