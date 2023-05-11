from django.urls import path, re_path, include
from event_app.views import MyView, EventsView, SingleEventView, OrganizedEventView, UpdateDeleteOrganizedEventView

urlpatterns = [
     path("", MyView.as_view(), name="my_view"),
     path("event/",SingleEventView.as_view(), name='event'),
     path("event/<int:event_id>", SingleEventView.as_view(), name='get-event'),
     path("events", EventsView.as_view(), name="events"),
     path("organization/<int:organization_id>/event/create", OrganizedEventView.as_view(), name= 'organized-event'),
     path("organization/<int:organization_id>/event/<int:event_id/", UpdateDeleteOrganizedEventView.as_view(), name='edit/delete-event')
]
