from django.shortcuts import render
from rest_framework import views, response
from ticket_app.serializers import TicketSerializer
from event_app import models, serializers
from ticket_app.models import Ticket
# Create your views here.

class CreateTicket(views.APIView):

    # permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        print(self.request)
        serializer = TicketSerializer(data=request.data)
        
        # if serializer.is_valid(raise_exception=True):
        #     serializer.save()
        return response.Response(data=serializer.data, status= 201)
        # return response.Response(data=serializer.errors, status = 400)
        
class GetAllTicketPerEvent(views.APIView):

    def get(self, request, event_id):
        tickets = Ticket.objects.filter(event=event_id)
        serializer = TicketSerializer(tickets, many=True)
        return response.Response(data=serializer.data, status= 200)
    
    def post(self, request):
        print(self.request.body)
        pass