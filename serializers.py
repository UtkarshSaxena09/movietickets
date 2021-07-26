from rest_framework import serializers
from movietickets.models import Movietickets, LANGUAGE_CHOICES, STYLE_CHOICES


class MovieticketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movietickets
        fields = ['id', 'booked', 'movie', 'ticketid']
