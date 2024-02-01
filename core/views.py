from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .permissions import SuperUserPermission
from .models import *
from .serializer import *


### SchoolModelViewSet ###

class SchoolMemberModelViewSet(ModelViewSet):
    permission_classes = [SuperUserPermission]
    queryset = SchoolMember.objects.all()
    serializer_class = SchoolMemberSerializer


    



### SchoolModelViewSet ###

class SchoolModelViewSet(ModelViewSet):
    permission_classes = [SuperUserPermission]
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
     
    @action(detail=True, methods=['get'])
    def user(self, request, pk=None):
        user_school = User.objects.filter(id=pk)
        serializer = UserSerializer(user_school)
        return Response(serializer.data)
    


        
    



### UserModelViewSet ###

class UserModelViewSet(ModelViewSet):
    permission_classes = [SuperUserPermission]
    queryset = User.objects.all()
    serializer_class = UserSerializer

          



