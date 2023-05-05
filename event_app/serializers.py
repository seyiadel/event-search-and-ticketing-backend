from rest_framework.serializers import ModelSerializer
from event_app.models import User, Event

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"