from django.shortcuts import render
# Create your views here.

from rest_framework import generics, permissions, authentication, views
from rest_framework.response import Response
from event_app.serializers import EventSerializer
from event_app.models import EventInfo
from organizations.models import Organization


class MyView(generics.ListAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        response = {
            'message': 'token works.',
            "data":request.user.email
        }
        return Response(response, status=200)

class SingleEventView(views.APIView):

    "Get Event for anonymous users"
    permission_classes = (permissions.AllowAny,)

    def get(self, request, event_id):
        event = EventInfo.objects.get(id=event_id)
        serializer = EventSerializer(event)
        return Response(data=serializer.data, status=200)



class EventsView(views.APIView):
    
    permission_classes = (permissions.AllowAny,)

    "Get all Events on the homepage"

    def get(self, request):
        event = EventInfo.objects.all()
        serializer = EventSerializer(event, many=True)
        return Response(data=serializer.data, status=200)

class OrganizedEventView(views.APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, organization_id):
        organizer =  Organization.objects.filter(id=organization_id).first()
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid(raise_exception= True):
            serializer.validated_data['organizer'] = organizer
            serializer.save()
            return Response(data=serializer.data, status=201)
        return Response(data=serializer.errors, status=400)

class UpdateDeleteOrganizedEventView(views.APIView):
     
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, organization_id, event_id):
        "Edit organized event per id"
        organization = Organization.objects.filter(id=organization_id).first()
        event = EventInfo.objects.filter(organizer=organization).get(id=event_id)
        serializer = EventSerializer(instance=event, data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(data=serializer.data, status=200)
        return Response(data=serializer.data, status=400)

    def delete(self, request, organization_id, event_id):
        organization = Organization.objects.filter(id=organization_id).first()
        event = EventInfo.objects.filter(organizer=organization).get(id=event_id)
        event.delete()
        return Response(data=F"Event{event.name}Deleted", status=200)