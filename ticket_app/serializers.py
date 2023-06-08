from rest_framework import serializers
from ticket_app.models import Ticket
from event_app.models import EventInfo
from tasks import charged_ticket_price


class TicketSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Ticket
        fields = "__all__"

    def create(self, validated_data):
        if validated_data['event'].type == "Free":
            validated_data['price'] = 0
            return Ticket.objects.create(**validated_data)
        validated_data['price'] = charged_ticket_price(validated_data['price'])
        return Ticket.objects.create(**validated_data)