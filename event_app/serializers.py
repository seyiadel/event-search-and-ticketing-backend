from rest_framework import serializers
from event_app.models import User, EventInfo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    tickets = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = EventInfo
        fields = ['name','description', 'artwork','venue', 'location','country','time','date','created_at','creator','tickets']