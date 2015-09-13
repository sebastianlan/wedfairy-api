from rest_framework import serializers
from rsvp.models import Rsvp, Guest

class RsvpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rsvp
        fields = ('id', 'message', 'deadline', 'created_date', 'changed_date')

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ('id', 'rsvp', 'avatar', 'name', 'people', 'created_date')



