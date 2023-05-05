from django.shortcuts import render
# Create your views here.

from rest_framework import generics
from rest_framework.response import Response


class MyView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        response = {
            'message': 'token works.',
            "data":request.headers
        }
        return Response(response, status=200)