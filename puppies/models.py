from django.db import models

# Create your models here.
class Puppy(models.Model):
    """
    Puppy models, define the attributes of a puppy
    """
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    breed = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_breed(self):
        return self.name + ' belong to ' + self.breed + ' breed.'
    
    def __repr__(self):
        return self.name + ' added.'
    
