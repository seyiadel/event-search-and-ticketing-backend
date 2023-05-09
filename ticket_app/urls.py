from django.urls import path
from ticket_app.views import CreateEventTicket,GetAllTicketPerEvent
urlpatterns = [
    path("event/<int:event_id>/tickets/create", CreateEventTicket.as_view(), name='create-ticket'),
    path("event/<int:event_id>/tickets", GetAllTicketPerEvent.as_view(), name='get-tickets')
]