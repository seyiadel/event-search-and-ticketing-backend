from rest_framework import serializers
from event_app.models import User, EventInfo
from ticket_app.serializers import TicketSerializer
from ticket_app.models import Ticket

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True)
    class Meta:
        model = EventInfo
        fields = ['id','name','description', 'artwork','venue', 'location','country','time','date','created_at','creator','tickets']

    def create(self, validated_data):
        ticket_data = validated_data.pop('tickets')
        event = EventInfo.objects.create(**validated_data)
        for ticket in ticket_data:
            create_ticket = Ticket.objects.create(event=event.pk,**validated_data)
        return event
