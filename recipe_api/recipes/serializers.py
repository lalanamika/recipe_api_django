from rest_framework import serializers
from recipes.models import Recipe
from django.contrib.auth.models import User

class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    
    class Meta:
        model = Recipe
        fields = ('url',
                  'id',
                  'recipe_name',
                  'ingredients',
                  'instructions',
                  'serving_size',
                  'category',
                  'notes',
                  'date_added',
                  'date_modified',
                  'author')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    recipes = serializers.HyperlinkedRelatedField(many=True,
                                                   view_name='recipe-detail',
                                                   read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'recipes')
