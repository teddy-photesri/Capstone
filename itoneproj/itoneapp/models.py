from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Emotion(models.Model):
    emotion_icon = models.ImageField(upload_to='images/')

class JournalEntry(models.Model):
    title = models.CharField(max_length=20)
    intensity = models.IntegerField()
    date_journal = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
