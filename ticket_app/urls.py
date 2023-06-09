from django.urls import path
from ticket_app.views import CreateEventTicket,GetAllTicketPerEvent
urlpatterns = [
    path("dashboard/events/<int:event_id>/tickets/create", CreateEventTicket.as_view(), name='create-ticket'),
    path("events/<int:event_id>/tickets", GetAllTicketPerEvent.as_view(), name='get-tickets')
]