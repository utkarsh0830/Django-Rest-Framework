from django.shortcuts import render
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def ItemView(request):
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        date = request.data
        serializer = ItemSerializer(data=date)
        if(serializer.is_valid):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    
