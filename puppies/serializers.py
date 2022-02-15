from django.forms import fields
from rest_framework import serializers
from .models import Puppy

class PuppySerializers(serializers.ModelSerializer):
    class Meta:
        model = Puppy
        fields = ('name', 'age', 'breed', 'color', 'created_at', 'updated_at')