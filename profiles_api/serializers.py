from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)
    
class UserProfileSerializer(serializers.ModelSerializer):
    """Serializers a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password', 'perfil', 'data','is_StarUser','is_staff')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }


    def create(self, validated_data):
        """Create and return a new userProfile"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password'],
            perfil=validated_data['perfil'],
            data=validated_data['data'],
        )
        print(validated_data)

        return user

class Userserializer(serializers.ModelSerializer):
    """ Serializa a criacao de equipe"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password', 'perfil', 'data','is_StarUser','is_staff')

    def create(self, validated_data,request):

        print(request.data)
        User_name = request.data.get("email")
        print(User_name)
        equipe = models.UserProfile.objects.create(self, email=User_name,**validated_data)   
