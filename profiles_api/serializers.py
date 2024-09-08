from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)  # Ensure 'name' is declared properly


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a UserProfile object"""
     # Define fields to include in the serialized output

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name','password')
        extra_kwargs = {
            'password': {
            'write_only': True,
                'style':{'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new UserProfile or return new user"""
        user = models.UserProfile.objects.create_user(
            email =validated_data['email'],
            name = validated_data['name'],
            password =validated_data['password']
        )
        return user





