from django.shortcuts import render
# Create your views here.

from rest_framework import generics, permissions
from rest_framework.response import Response


class MyView(generics.ListAPIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        response = {
            'message': 'token works.',
            "data":request.user.username
        }
        return Response(response, status=200)