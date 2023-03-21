from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Room, RoomSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/v1',
        'GET /api/v1/rooms',
        'GET /api/v1/rooms/:id',
    ]
    return Response(routes)


# GET /api/v1/rooms
@api_view(['GET'])
def getRooms(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        context = {
            'success': True,
            'message': 'get rooms successfully',
            'data': serializer.data
        }
        return Response(context)


# GET /api/v1/rooms/:id
@api_view(['GET'])
def getRoom(request, pk):
    if request.method == 'GET':
        room = Room.objects.get(pk=pk)
        serializer = RoomSerializer(room)
        context = {
            'success': True,
            'message': 'get room successfully',
            'room': serializer.data
        }
        return Response(context)
