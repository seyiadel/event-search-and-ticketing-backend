from django.urls import path
from ticket_app.views import CreateEventTicket,GetAllTicketPerEvent, GetEventAttendeeDetails
urlpatterns = [
    path("dashboard/events/<int:event_id>/tickets/create", CreateEventTicket.as_view(), name='create-ticket'),
    path("events/<int:event_id>/tickets", GetAllTicketPerEvent.as_view(), name='get-tickets'),
    path("tickets/<int:ticket_id>/event-attendees/", GetEventAttendeeDetails.as_view(), name="event-attendee")
]