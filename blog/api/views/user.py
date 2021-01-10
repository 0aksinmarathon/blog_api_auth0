from rest_framework.viewsets import ModelViewSet
from blog.modules.user.models import User
from blog.modules.user.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
