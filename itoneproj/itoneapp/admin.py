from django.contrib import admin
from .models import Emotion, JournalEntry

admin.site.register(Emotion)
admin.site.register(JournalEntry)
