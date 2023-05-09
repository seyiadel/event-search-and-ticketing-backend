from rest_framework import serializers
from ticket_app.models import Ticket
from event_app.models import EventInfo


class TicketSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Ticket
        fields = "__all__"

    