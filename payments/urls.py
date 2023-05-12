from django.urls import path
from payments.views import CheckOutView, WebHookView, OrganzationBankDetails, ListBanks


urlpatterns = [
    path("ticket/<int:ticket_id>/checkout", CheckOutView.as_view(), name='checkout'),
    path("webhook/", WebHookView.as_view(), name="webhook"),
    path("organization/<int:organization_id>/add_bank_detail/", OrganzationBankDetails.as_view(), name='bank_detail'),
    path("list_banks/", ListBanks.as_view(), name="banks")
]