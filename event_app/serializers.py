from rest_framework import serializers
from event_app.models import User, EventInfo
from ticket_app.serializers import TicketSerializer
from ticket_app.models import Ticket

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = EventInfo
        fields = ['id','name','description', 'artwork','venue', 'location','country','type','start_time','start_date','end_time','end_date','created_at','organizer','earnings', 'is_published']

