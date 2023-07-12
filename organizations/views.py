from rest_framework import views, response, permissions
from organizations.serializers import OrganizationSerializer
from organizations.models import Organization
from drf_yasg.utils import swagger_auto_schema
from knox.auth import TokenAuthentication as KnoxTokenAuthentication
# Create your views here.

class OrganizationView(views.APIView):

    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [KnoxTokenAuthentication,]

    @swagger_auto_schema(request_body=OrganizationSerializer)
    def post(self, request):
        
        "Create a new Organization"

        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['creator'] = request.user
            serializer.save()
            return response.Response(data=serializer.data, status=201)
        return response.Response(data=serializer.errors, status=400)

    @swagger_auto_schema(OrganizationSerializer)
    def get(self, request):
        "Get all Organizations by Logged In User"
        organization = Organization.objects.filter(creator=request.user)
        serializer = OrganizationSerializer(organization, many=True)
        return response.Response(data=serializer.data, status=200)


class SingleOrganizationView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [KnoxTokenAuthentication,]

    @swagger_auto_schema(OrganizationSerializer)
    def get(self, request, organization_id):
        organization = Organization.objects.filter(creator=request.user).get(uuid=organization_id)
        serializer = OrganizationSerializer(organization)
        return response.Response(data=serializer.data, status=200)

