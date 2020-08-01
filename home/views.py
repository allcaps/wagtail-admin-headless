from .models import HomePage
from .serializers import HomePageSerializer
from rest_framework import viewsets
from rest_framework import permissions


class HomePageViewSet(viewsets.ModelViewSet):
    queryset = HomePage.objects.all()
    serializer_class = HomePageSerializer
    permission_classes = [permissions.IsAdminUser]
