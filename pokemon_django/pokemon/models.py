from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .services import get_username

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='ash.png')

    def __str__(self):
        return f'Perfil de {self.user.username}'

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    rival = models.CharField(max_length=100, default=get_username())
    resultado = models.CharField(max_length=20)
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f'{self.user.username}: {self.content}'

#class Pokemones(models.Model):
 #   user = models.OneToOneField(User, on_delete=models.CASCADE)
  #  image = models.ImageField()
   # name = models.CharField(max_length=100)


