from rest_framework import permissions, views
from rest_framework.response import Response
from event_app.serializers import EventSerializer, UserSerializer, LoginUserSerializer
from event_app.models import EventInfo
from organizations.models import Organization
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication as KnoxTokenAuthentication
from knox.models import AuthToken


class MyView(views.APIView):
    permission_classes = [permissions.IsAuthenticated,]
    authentication_classes =[KnoxTokenAuthentication,]

    def get(self, request):
        return Response(data={'user':request.user.email})
    

class SignUpView(views.APIView):
    permission_classes = [permissions.AllowAny,]

    @swagger_auto_schema(request_body=UserSerializer)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=200)
        return Response(serializer.errors)

class LogInView(KnoxLoginView):

    permission_classes = [permissions.AllowAny,]
    
    @swagger_auto_schema(request_body=LoginUserSerializer)
    def post(self, request):
       serializer = LoginUserSerializer(data=request.data)
       if serializer.is_valid(raise_exception=True):
           user = serializer.validated_data['user']
           login(request, user)
           return Response(data={
               "token": AuthToken.objects.create(user)[1],
               "first_name": request.user.first_name,
               "last_name":request.user.last_name
           }, status= 200)
           


    

class SingleEventView(views.APIView):

    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(EventSerializer)
    def get(self, request, event_id):
        "Get Event for anonymous users"
        event = EventInfo.objects.get(id=event_id)
        serializer = EventSerializer(event)
        return Response(data=serializer.data, status=200)



class EventsView(views.APIView):
    
    permission_classes = (permissions.AllowAny,)

    
    @swagger_auto_schema(EventSerializer())
    def get(self, request):
        "Get all Events on the homepage"
        event = EventInfo.objects.filter(is_published=True)
        serializer = EventSerializer(event, many=True)
        return Response(data=serializer.data, status=200)

class CreateEventView(views.APIView):
    """Logged In User to create events"""
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [KnoxTokenAuthentication,]

    @swagger_auto_schema(request_body=EventSerializer)
    def post(self, request, organization_id):
        organizer =  Organization.objects.filter(creator=request.user).first()
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid(raise_exception= True):
            serializer.validated_data['organizer'] = organizer
            serializer.save()
            return Response(data=serializer.data, status=201)
        return Response(data=serializer.errors, status=400)

class PublishEvents(views.APIView):

    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [KnoxTokenAuthentication,]

    @swagger_auto_schema(request_body=EventSerializer)
    def put(self, request, organization_id, event_id):
        organization = Organization.objects.filter(creator=request.user).get(id=organization_id)
        event = EventInfo.objects.filter(organizer=organization).get(id=event_id)
        serializer = EventSerializer(instance=event, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['is_published'] = True
            serializer.save()
            return Response(data= serializer.data, status = 200)
        return Response(data=serializer.errors, status= 400)

class UpdateDeleteOrganizedEventView(views.APIView):
     
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [KnoxTokenAuthentication,]

    @swagger_auto_schema(request_body=EventSerializer)
    def put(self, request, organization_id, event_id):
        "Edit organized event per id"
        organization = Organization.objects.filter(creator=request.user).get(id=organization_id)
        event = EventInfo.objects.filter(organizer=organization).get(id=event_id)
        serializer = EventSerializer(instance=event, data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(data=serializer.data, status=200)
        return Response(data=serializer.data, status=400)

    @swagger_auto_schema(EventSerializer)
    def delete(self, request, organization_id, event_id):
        organization = Organization.objects.filter(creator=request.user).get(id=organization_id)
        event = EventInfo.objects.filter(organizer=organization).get(id=event_id)
        event.delete()
        return Response(data=F"Event {event.name} Deleted", status=200)

class OrganizationEvents(views.APIView):

    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [KnoxTokenAuthentication,]

    @swagger_auto_schema(EventSerializer)
    def get(self, request, organization_id):
        """Get all Events associated to the Organization"""
        organizer =  Organization.objects.filter(creator=request.user).first()
        events = EventInfo.objects.filter(organizer=organizer)
        serializer = EventSerializer(events, many=True)
        return Response(data=serializer.data, status=201)
        