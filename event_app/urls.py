from django.urls import path, re_path, include
from event_app.views import MyView


urlpatterns = [
     path("", MyView.as_view(), name="my_view")
]

