from django.shortcuts import render
from rest_framework import views, response
from ticket_app.models import Ticket
from payments.serializers import CheckoutSerializer
import requests
from event_core import settings
# Create your views here.


def paystack_charge(email, amount, ticket_event_name):
    url = "https://api.paystack.co/transaction/initialize"
    headers= {"Authorization":f"Bearer {settings.PAYSTACK_SECRET_KEY}"}
    data = {"email": email,
    "amount": amount,
    }
    process = requests.post(url=url, headers=headers, data=data)
    return process


class CheckOutView(views.APIView):
     
    def post(self, request, ticket_id):
        ticket = Ticket.objects.filter(id=ticket_id).first()
        print(ticket)
        if not ticket:
            return response.Response(data="Ticket do not exist and not assigned to event", status=404)
        serializer = CheckoutSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(serializer.validated_data)
            serializer.validated_data['ticket'] = ticket
            email = serializer.validated_data['user']
            ticket_event_name = ticket.event.name
            amount = ticket.price * serializer.validated_data['quantity'] *100
            payment_detail=paystack_charge(email, amount, ticket_event_name)
            serializer.save()
            return response.Response(data={"data":serializer.data, "payment_detail": payment_detail}, status=200)
        return response.Response(data=serializer.errors, status=400)