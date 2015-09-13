from rest_framework import serializers
from map.models import Map

class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ('id', 'location', 'address', 'message', 'map_lng', 'map_lat', 'created_date', 'changed_date')




