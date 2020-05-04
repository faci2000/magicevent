from .models import Client,Event
from rest_framework import serializers 

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields =['id','title','start_date','end_date','thumbnail',]

class ClientSerializer(serializers.ModelSerializer):
    events = EventSerializer(read_only=True, many=True)
    class Meta:
        model = Client
        fields = ['id', 'name','surname','mail','events',]