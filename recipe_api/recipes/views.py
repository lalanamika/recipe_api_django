from recipes.models import Recipe
from recipes.serializers import RecipeSerializer, UserSerializer
from rest_framework import viewsets, permissions
from django.contrib.auth.models import User
from recipes.permissions import IsOwnerOrReadOnly

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset= User.objects.all()
    serializer_class = UserSerializer
