from django.urls import path
from payments.views import CheckOutView


urlpatterns = [
    path("ticket/<int:ticket_id>/checkout", CheckOutView.as_view(), name='checkout')
]