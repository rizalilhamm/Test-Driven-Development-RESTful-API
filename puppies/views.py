from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Puppy
from .serializers import PuppySerializers

# Create your views here.
@api_view(['GET', 'UPDATE', 'DELETE'])
def get_update_delete_puppy(request, pk):
    try:
        puppy = Puppy.objects.get(pk=pk)
    except Puppy.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response({})
    elif request.method == 'DELETE':
        return Response({})
    elif request.method == 'PUT':
        return Response({})

@api_view(['GET', 'POST'])
def get_post_puppies(request):
    # Get all puppies
    # if request.method == 'GET':
        # return Response({})
    # Insert a new record for a puppy
    # elif request.method == 'POST':
        # return Response({})
    if request.method == 'GET':
        puppies = Puppy.objects.all()
        serializer = PuppySerializers(puppies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        return Response({})