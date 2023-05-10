from django.shortcuts import render
from rest_framework import views, response
from ticket_app.models import Ticket
from payments.serializers import CheckoutSerializer
import requests
from event_core import settings
from payments.models import Checkout
# Create your views here.


def paystack_charge(email, amount):
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
        if not ticket:
            return response.Response(data="Ticket do not exist and not assigned to event", status=404)
        serializer = CheckoutSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['ticket'] = ticket
            email = serializer.validated_data['user']
            ticket_pre_detail= f"{ticket.event.name} -{ticket.status}"
            print(ticket_pre_detail)
            amount = ticket.price * serializer.validated_data['quantity'] *100
            payment_detail=paystack_charge(email, amount)
            serializer.validated_data['status'] = "Pending"
            serializer.save()
            return response.Response(data={"tick":serializer.data, "pay":payment_detail}, status=200)
        return response.Response(data=serializer.errors, status=400)



class WebHookView(views.APIView):
    def post(self,request):
        if request.data['event'] == "charge.success":
           checkout = Checkout.objects.filter(user=request.data['data']['customer']['email'])
           checkout.update(status="Paid")
           return response.Response(status=200)
        else:
            checkout.update(status="Failed")
            return response.Response(status=404)


