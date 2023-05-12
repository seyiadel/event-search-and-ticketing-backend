from django.shortcuts import render
from rest_framework import views, response
from ticket_app.models import Ticket
from payments.serializers import CheckoutSerializer, BankDetailSerializer
from payments.models import Checkout
from tasks import paystack_charge , list_banks
from organizations.models import Organization
# Create your views here.




class CheckOutView(views.APIView):
     
    def post(self, request, ticket_id):
        ticket = Ticket.objects.filter(id=ticket_id).first()
        if not ticket:
            return response.Response(data="Ticket do not exist and not assigned to event", status=404)
        serializer = CheckoutSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['ticket'] = ticket
            email = serializer.validated_data['user']
            amount = ticket.price * serializer.validated_data['quantity'] *100
            payment_detail=paystack_charge(email, amount)
            serializer.validated_data['status'] = "Pending"
            serializer.validated_data['amount'] = amount/100
            serializer.validated_data['paystack_reference'] = payment_detail['data']['reference']
            serializer.save()
            return response.Response(data={"checkout":serializer.data, "pay":payment_detail}, status=200)
        return response.Response(data=serializer.errors, status=400)



class WebHookView(views.APIView):
    def post(self,request):
        if request.data['event'] == "charge.success":
            # Log here - Request charge was a success
           checkout = Checkout.objects.get(user=request.data['data']['customer']['email'])
           checkout.status = "Paid"
           checkout.save()
           tickets = Ticket.objects.get(id=checkout.ticket.id)
           tickets.available_tickets -= checkout.quantity
           tickets.save()
           return response.Response(status=200)
        elif request.data['event'] == "transfer.success":
            print(request.data)
        # checkout.update(status="Failed")
        return response.Response(status=404)


class OrganzationBankDetails(views.APIView):

    def post(self, request, organization_id):
        organization = Organization.objects.get(id=organization_id)
        serializer = BankDetailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):     
          serializer.validated_data['owner'] = organization
          serializer.save()
          return response.Response(data=serializer.data, status=201)
        return response.Response(data=serializer.errors, status=400)
        


class ListBanks(views.APIView):

    def get(self, request):
        banks = list_banks()
        return response.Response(data=banks)
    