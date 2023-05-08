from django.urls import path
from ticket_app.views import CreateTicket,GetAllTicketPerEvent
urlpatterns = [
    path("create-ticket", CreateTicket.as_view(), name='create-ticket'),
    path("event/<int:event_id>/tickets", GetAllTicketPerEvent.as_view(), name='get-tickets')
]