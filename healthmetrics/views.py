from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from .models import HealthMetrik
from .serializers import HealthMetrikSerializer
from .pagination import HealthMetrikPagination


class HealthMetrikViewSet(viewsets.ModelViewSet):
    queryset = HealthMetrik.objects.all()
    serializer_class = HealthMetrikSerializer
    pagination_class = HealthMetrikPagination
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)