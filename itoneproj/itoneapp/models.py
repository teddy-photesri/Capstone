from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.username

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
        return self.user.username + ' ' + str(self.emotion) + " " + self.content[:20] +  " " + str(self.date_journal)
