from rest_framework.serializers import ModelSerializer
from ticket_app.models import Ticket


class TicketSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"

    def create(self, validated_data):
        return Ticket.objects.create(**validated_data)