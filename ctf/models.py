from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class Stage(models.Model):
    class Meta:
        ordering = ['title']

    title = models.CharField('標題', max_length=1)
    flag = models.CharField(max_length=256)
    def __str__(self):
        return self.title

class Participant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    cleared_stages = models.ManyToManyField(Stage, blank=True)
    submit_time = models.DateTimeField(auto_now=True)

def create_participant(sender, instance, created, **kwargs):
    if created:
        Participant.objects.create(user=instance)

post_save.connect(create_participant, sender=User)
