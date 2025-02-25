from .models import CustomUserModel
from rest_framework import viewsets
from .serializers import UserSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset = CustomUserModel.objects.all()
    serializer_class = UserSerializer
