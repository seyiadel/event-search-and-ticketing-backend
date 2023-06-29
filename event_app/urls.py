from django.urls import path, re_path, include
from event_app.views import MyView,EventsView, SingleEventView, CreateEventView, UpdateDeleteOrganizedEventView, OrganizationEvents, SignUpView, LogInView
from knox import views

urlpatterns = [
     path('sign-up/',SignUpView.as_view(), name='signup_view'),
     path('login/', LogInView.as_view(), name='login'),
     path('logout/',views.LogoutView.as_view(), name= "knox-logout"),
     path("", MyView.as_view(), name="my_view"),
     path("events/<int:event_id>", SingleEventView.as_view(), name='get-event'),
     path("events", EventsView.as_view(), name="events"),
     path("dashboard/organization/<int:organization_id>/event/create", CreateEventView.as_view(), name= 'organized-event'),
     path("dashboard/organization/<int:organization_id>/event/<int:event_id>/", UpdateDeleteOrganizedEventView.as_view(), name='edit/delete-event'),
     path("dashboard/organization/<int:organization_id>/events", OrganizationEvents.as_view(), name= 'event-by-organization'),
]
