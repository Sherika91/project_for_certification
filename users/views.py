from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import User
from users.permissions import IsOwnerOrAdmin, IsAdmin
from users.serializers import UserSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    default_permission = [AllowAny]
    permissions = {
        'list': [IsAdmin],
        'retrieve': [IsAuthenticated, IsOwnerOrAdmin],
        'create': [],
        'update': [IsOwnerOrAdmin],
        'partial_update': [IsOwnerOrAdmin],
        'destroy': [IsOwnerOrAdmin],
    }

    def get_permissions(self):
        return [permission() for permission in self.permissions.get(self.action, self.default_permission)]
