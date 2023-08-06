from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Animal
from .serialisers import ItemSreialiser


@api_view(['GET'])
def getData(request):
    # To return the current locations of all the animals 
       
    items = Animal.objects.all()
    serialiser = ItemSreialiser(items, many=True)
    
    return Response(serialiser.data)

@api_view(['POST'])
def addGps(request):
    # to add a new animal or update existing ones 
    
    data = request.data
    
    a = Animal.objects.create(id = data["id"], lat=data["Lat"], longitude=data["Long"])
    a.save()
    print(a)
    
    return Response()

    
    
    
    
    
    
