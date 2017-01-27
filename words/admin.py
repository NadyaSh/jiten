from django.contrib import admin
from .models import Base, Word, SubWord

admin.site.register(Base)
admin.site.register(Word)
admin.site.register(SubWord)

# Register your models here.
