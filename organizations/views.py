from django.shortcuts import render
from rest_framework import views, response
from organizations.serializers import OrganizationSerializer
from organizations.models import Organization

# Create your views here.

class OrganizationView(views.APIView):

    def post(self, request):
        
        "Create a new Organization"

        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return response.Response(data=serializer.data, status=201)
        return response.Response(data=serializer.errors, status=400)

    def get(self, request):
        "Get all Organizations by Logged In User"
        organization = Organization.objects.filter(creator=request.user)
        serializer = OrganizationSerializer(organization, many=True)
        return response.Response(data=serializer.data, status=200)


class SingleOrganizationView(views.APIView):

    def get(self, request, organization_id):
        organization = Organization.objects.filter(creator=request.user).get(id=organization_id)
        serializer = OrganizationSerializer(organization)
        return response.Response(data=serializer.data, status=200)
