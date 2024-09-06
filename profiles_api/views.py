from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """A simple API view"""

    def get(self, request, format=None):
        """Return a simple message"""
        an_apiview = [
            'Use HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
