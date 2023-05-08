from django.urls import path, re_path, include
from event_app.views import MyView, EventsView, SingleEventView


urlpatterns = [
     path("", MyView.as_view(), name="my_view"),
     path("event/",SingleEventView.as_view(), name='event'),
     path("event/<int:pk>", SingleEventView.as_view(), name='get-event'),
     path("events", EventsView.as_view(), name="events"),
]

