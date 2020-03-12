from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Emotion(models.Model):
    emotion_icon = models.ImageField(upload_to='images/')
    emotion_name = models.CharField(max_length=10)

    def __str__(self):
        return self.emotion_name

class JournalEntry(models.Model):
    emotion = models.ForeignKey(Emotion, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    intensity = models.IntegerField()
    content = models.TextField()
    date_journal = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content[:20]
