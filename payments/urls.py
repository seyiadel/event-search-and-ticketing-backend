from django.urls import path
from payments.views import CheckOutView, WebHookView, OrganzationBankDetails, ListBanks, WithdrawEarningsView


urlpatterns = [
    path("ticket/<int:ticket_id>/checkout", CheckOutView.as_view(), name='checkout'),
    path("webhook/", WebHookView.as_view(), name="webhook"),
    path("organization/<int:organization_id>/add_bank_detail/", OrganzationBankDetails.as_view(), name='bank_detail'),
    path("list_banks/", ListBanks.as_view(), name="banks"),
    path("organization/<int:organization_id>/events/<int:event_id>/withdraw/", WithdrawEarningsView.as_view(), name ="withdraw"),
]