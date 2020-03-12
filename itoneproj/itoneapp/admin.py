from django.contrib import admin
from .models import Emotion, JournalEntry, User

admin.site.register(Emotion)
admin.site.register(JournalEntry)
admin.site.register(User)
