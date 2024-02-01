from django.db import router
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

routers = DefaultRouter()

routers.register(r'user', UserModelViewSet, basename = 'user')

routers.register(r'school', SchoolModelViewSet, basename = 'school')

routers.register(r'members', SchoolMemberModelViewSet, basename = 'member')

urlpatterns = routers.urls
