from django.shortcuts import render
from rest_framework import views, response, permissions
from ticket_app.serializers import TicketSerializer
from event_app import models
from ticket_app.models import Ticket
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class CreateEventTicket(views.APIView):

    permission_classes = (permissions.IsAuthenticated,)

    @swagger_auto_schema(request_body=TicketSerializer)
    def post(self, request, event_id):
        event = models.EventInfo.objects.filter(id=event_id).first()
        if not event:
            return response.Response(data=f"Event {event_id} do not exist", status=404)
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['event'] = event
            serializer.save()
            return response.Response(data=serializer.data, status= 201)
        return response.Response(data=serializer.errors, status = 400)
        
class GetAllTicketPerEvent(views.APIView):

    def get(self, request, event_id):
        tickets = Ticket.objects.filter(event=event_id)
        serializer = TicketSerializer(tickets, many=True)
        return response.Response(data=serializer.data, status= 200)
    

