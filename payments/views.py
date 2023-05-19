from django.shortcuts import render
from rest_framework import views, response
from ticket_app.models import Ticket
from payments.serializers import CheckoutSerializer, BankDetailSerializer, WithdrawEventEarningSerializer
from payments.models import Checkout, EventInfo, BankDetail, ListOfBank, WithdrawEventEarning
from tasks import paystack_charge , list_banks, tranfer_earnings, remove_charge_from_earnings
from organizations.models import Organization
import uuid
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
           charge_free_earning = remove_charge_from_earnings(checkout.amount)
           tickets.total_checkout_amount += checkout.amount
           tickets.event.earnings += charge_free_earning
           tickets.save()
           return response.Response(status=200)
        elif request.data['event'] == "transfer.success":
            payout = WithdrawEventEarning.objects.get(reference_code=request.data['data']['reference'])
            payout.event.earnings -= request.data['data']['amount']
            payout.status == "Transfer Successful"
            payout.save()
            print(request.data)
            return response.Response(status=200)
        elif request.data['event'] == "transfer.failed":
            retry_payout = WithdrawEventEarning.objects.get(reference_code=request.data['data']['reference'])
            amount= retry_payout.event.earnings * 100
            recipient_code = retry_payout.bank_detail.recipient_code
            unique_reference = retry_payout.reference_code
            reason = {f"Payout for {retry_payout.event.name} earnings of {retry_payout.event.earnings}"}
            tranfer_earnings(amount, recipient_code, unique_reference, reason)
            retry_payout.status == "Transfer Failed"
            retry_payout.save()
            return response.Response(status=200)
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
    

class WithdrawEarningsView(views.APIView):

    def post(self, request,organization_id, event_id):
        organization = Organization.objects.get(id=organization_id)
        event = EventInfo.objects.filter(organizer=organization).get(id=event_id)
        bank_detail = BankDetail.objects.get(owner=organization)
        serializer = WithdrawEventEarningSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['event'] = event
            serializer.validated_data['bank_detail'] = bank_detail
            reason = {f"Payout for {event.name} earnings of {event.earnings}"}
            reference_code = uuid.uuid4()
            amount = event.earning * 100
            payout = tranfer_earnings(amount, bank_detail.recipient_code, reference_code, reason)   
            serializer.validated_data['reference_code'] = payout['data']['reference']
            serializer.save()
            return response.Response(data={serializer.data, payout}, status= 201)
        return response.Response(data=serializer.errors, status= 400)