import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Puppy
from ..serializers import PuppySerializers


# Initialize the APIClient app
client = Client()

class GetAllPuppiesTest(TestCase):
    """
    Test module for GET all puppies api
    """
    def setUp(self):
        Puppy.objects.create(name='Casper', age=3, breed='Bull dog', color='Black')
        Puppy.objects.create(name='Muffin', age=1, breed='Gradane', color='Brown')
        Puppy.objects.create(name='Rambo', age=2, breed='Labrador', color='Black')
        Puppy.objects.create(name='Ricky', age=6, breed='Labrador', color='Brown')
    
    def test_get_all_puppies(self):
        # Get API response
        response = client.get(reverse('get_post_puppies'))
        # get data from DB
        puppies = Puppy.objects.all()
        print("Puppies", puppies)
        serializer = PuppySerializers(puppies, many=True)
        print("serializer ", serializer)
        # for i in serializer.data:
            # print("Serializr data", i)
        print(response.data)
        
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    