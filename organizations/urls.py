from django.urls import path
from organizations.views import OrganizationView

urlpatterns =[
    path("organization/create", OrganizationView.as_view(), name="organisation"),
]