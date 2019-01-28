from django.db import models

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    ingredients = models.TextField()
    instructions = models.TextField()
    serving_size = models.PositiveIntegerField(blank=True, default=1)
     # category should be a list to choose from
    category = models.CharField(max_length=200, blank=True, default='main course')
    notes = models.TextField(blank=True, default='')
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', related_name='recipes', on_delete=models.CASCADE)

    class Meta:
        ordering = ('date_modified',)
