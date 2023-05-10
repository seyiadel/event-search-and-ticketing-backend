from django.urls import path
from payments.views import CheckOutView, WebHookView


urlpatterns = [
    path("ticket/<int:ticket_id>/checkout", CheckOutView.as_view(), name='checkout'),
    path("webhook/", WebHookView.as_view(), name="webhook")
]