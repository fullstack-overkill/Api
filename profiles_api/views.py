from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as funcion (get, post, patch, put, delete)',
            'Is similar to a tradicional Djando View',
            'Gives you the most control over you aplication logic',
            'Is mapped manually to URLs'
        ]


        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
    
    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST        )
    
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle a partial update of and object"""
        return Response({'method': "PACTH"})
    
    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'delete'})

class HelloViewset(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})
    
    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrive(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, requet, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})        
    
    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})
    
    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'Delete' })

class UserProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = ( permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
    
    
    

class UserLoginApiView(ObtainAuthToken):
    """Gandle creating user authentication tokens"""
    
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class userView(APIView):
    #permission_classes = (IsAuthenticated,)
    
    def get(self, request,format=None):
        print(request.user)
        print("SADSDASDASDASD")
        username = request.user
        print(username)
        equipe = models.UserProfile.objects.filter(email=username)
        serializer = serializers.UserProfileSerializer(equipe,many=True)
        
        return Response(serializer.data)

    
    def post(self, request):
        serializer = serializers.Userserializer(data=request.data)
        #serializer.is_valid(raise_exception=ValueError)
        serializer.create(validated_data=request.data, request=request)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    """
    def put(self, request):
        serializer = serializers.SquadSerializer(data=request.data)       
        serializer.update(validated_data=request.data, request=request)
        return Response(serializer.initial_data)

    def patch(self, request):
        serializer = serializers.SquadSerializer(data=request.data)       
        serializer.patch(validated_data=request.data, request=request)
        return Response(serializer.initial_data)
    """