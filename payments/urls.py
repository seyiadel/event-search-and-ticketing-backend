from django.urls import path
from payments.views import CheckOutView, WebHookView, OrganzationBankDetails, ListBanks, WithdrawEarningsView


urlpatterns = [
    path("ticket/<int:ticket_id>/checkout", CheckOutView.as_view(), name='checkout'),
    path("webhook/", WebHookView.as_view(), name="webhook"),
    path("dashboard/organization/<int:organization_id>/add-bank-detail/", OrganzationBankDetails.as_view(), name='bank_detail'),
    path("list_banks/", ListBanks.as_view(), name="banks"),
    path("dashboard/organization/<int:organization_id>/events/<int:event_id>/withdraw-earnings/", WithdrawEarningsView.as_view(), name ="withdraw"),
]