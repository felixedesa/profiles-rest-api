from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api.serializers import HelloSerializer  # Import the serializer class

class HelloApiView(APIView):
    """A simple API view"""
    serializer_class = HelloSerializer

    def get(self, request):
        """Return a simple message"""
        an_apiview = [
            'Use HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})
    def post(self, request):
        """Create a Hello Message With Our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            return Response({'message': f'Hello, {name}!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handling Updating Entire object """
        return Response({'method': 'PUT'})



    def patch(self, request, pk=None):
        """Handling Updating Particular fields of object """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Handling Deleting an object """
        return Response({'method': 'DELETE'})