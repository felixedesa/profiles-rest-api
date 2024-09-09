from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from profiles_api.serializers import HelloSerializer,UserProfileSerializer,ProfileFeedItemSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings

from profiles_api import models
from profiles_api import permissions
from rest_framework import filters

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

class HelloViewSet(viewsets.ViewSet):
    """A viewset for viewing and editing Hello objects"""
    serializer_class = HelloSerializer

    def list(self, request):
        """Return Hello Message"""
        an_apiviewset = [
            'Uses actions (list, create, retrieve, update, partial_update, destroy)',
            'Automatically maps to URLs using routers',
            'Provides more functionality with less code',
        ]
        return Response({'message': 'Hello', 'an_apiviewset': an_apiviewset})

    def create(self, request):
        """Create a Hello Message With Our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data['name']
            return Response({'message': f'Hello, {name}!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handling Retrieving a particular object """
        return Response({'method': 'GET'})

    def update(self, request, pk=None):
        """Handling Updating Entire object """
        return Response({'method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handling Updating Particular fields of object """
        return Response({'method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handling Deleting an object """
        return Response({'method': 'DELETE'})



class UserProfileViewSet(viewsets.ModelViewSet):
    """A viewset for viewing and editing UserProfile objects or updating and creating profiles"""
    serializer_class = UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
    ordering_fields = ('id', 'email', 'name',)
    ordering = ('id',)

    def perform_create(self, serializer):
        """Create a new UserProfile"""
        return serializer.save()

    def perform_update(self, serializer):
        """Update an existing UserProfile"""
        return serializer.save()

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES



class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """A viewset for viewing and editing ProfileFeedItem objects"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = [permissions.UpdateOwnProfile,IsAuthenticated]

    def perform_create(self, serializer):
        """Create a new profile feed item"""
        serializer.save(user_profile=self.request.user)



