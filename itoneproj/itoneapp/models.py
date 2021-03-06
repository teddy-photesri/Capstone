from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    profile_image = models.ImageField(upload_to='images/',null=True, blank=True)

    def __str__(self):
        return self.username

class Emotion(models.Model):
    icon = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=10)
    color = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class JournalEntry(models.Model):
    emotion = models.ForeignKey(Emotion, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    intensity = models.IntegerField()
    content = models.TextField()
    date_journal = models.DateTimeField(default=timezone.now)

    def time(self):
        return str(self.date_journal)

    class Meta:
        ordering = ['-date_journal']

    def __str__(self):
        return self.user.username + ' ' + str(self.emotion) + " " + str(self.date_journal)
