from django.urls import path
from organizations.views import OrganizationView, SingleOrganizationView

urlpatterns =[
    path("organization/create", OrganizationView.as_view(), name="organisation"),
    path("dashboard/organization/<int:organization_id>/", SingleOrganizationView.as_view(), name="get_organization")
]