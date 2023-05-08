from django.shortcuts import render
# Create your views here.

from rest_framework import generics, permissions, authentication, views
from rest_framework.response import Response
from event_app.serializers import EventSerializer
from event_app.models import EventInfo


class MyView(generics.ListAPIView):

    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request, *args, **kwargs):
        response = {
            'message': 'token works.',
            "data":request.user.email
        }
        return Response(response, status=200)

class SingleEventView(views.APIView):

    # permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid(raise_exception= True):
            serializer.save()
            return Response(data=serializer.data, status=201)
        return Response(data=serializer.errors, status=400)

    def get(self, request, pk):
        event = EventInfo.objects.get(id=pk)
        serializer = EventSerializer(event)
        return Response(data=serializer.data, status=200)

class EventsView(views.APIView):
    
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        event = EventInfo.objects.all()
        serializer = EventSerializer(event, many=True)
        return Response(data=serializer.data, status=200)
