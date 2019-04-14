from django.shortcuts import render

from rest_framework.views import APIView # Imports APIView class from the rest_framework.views Module

from rest_framework.response import Response # Imports Response object/class from the rest_framework.response Module
# Create your views here.

# Code that gets run when the user visits our API endpoint;

# Define a new class HelloAPIView and inherit from APIView:

class HelloAPIView(APIView):
    """ Test API View"""

    def get(self, request, format):
        """Resturns a list of API features"""

        an_apiview = [
        'Uses HTTP Methods as function ( get, post, patch, put, delete)',
        'Gives most control over your logic',
        'Is mapped manually to URLs'
        ]

        return Response({'Message': 'Hello', 'An APIView': an_apiview})
