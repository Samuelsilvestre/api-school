from dataclasses import fields
from rest_framework import serializers
from .models import User, School, SchoolMember

class SchoolMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = SchoolMember
        fields = '__all__'

### SchoolSerializer ###
class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = '__all__'

## UserSerializer ##
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password'
        ]

