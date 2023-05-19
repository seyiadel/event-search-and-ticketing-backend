from django.shortcuts import render
from rest_framework import views, response, permissions
from organizations.serializers import OrganizationSerializer
from organizations.models import Organization
from tasks import verify_bank_details, create_tranfer_recipient
# Create your views here.

class OrganizationView(views.APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        
        "Create a new Organization"

        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return response.Response(data=serializer.data, status=201)
        return response.Response(data=serializer.errors, status=400)

    def get(self, request):
        "Get all Organizations by Logged In User"
        organization = Organization.objects.all() #(creator=request.user)
        serializer = OrganizationSerializer(organization, many=True)
        return response.Response(data=serializer.data, status=200)


class SingleOrganizationView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, organization_id):
        organization = Organization.objects.get(id=organization_id)
        serializer = OrganizationSerializer(organization)
        return response.Response(data=serializer.data, status=200)


