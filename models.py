from django.db import models

class Movietickets(models.Model):
    booked = models.DateTimeField(auto_now_add=True)
    movie = models.CharField(max_length=100, blank=True, default='')
    ticketid = models.TextField()
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()
    