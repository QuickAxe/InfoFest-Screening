from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Animal
from .serialisers import ItemSreialiser


@api_view(['GET'])
def getData(request):
    # sample api json to return 
    #person = {'name' : 'Foo', 'address' : 'bar'}
    
    items = Animal.objects.all()
    serialiser = ItemSreialiser(items, many=True)
    
    return Response(serialiser.data)

@api_view(['POST'])
def addItem(request):
   
    #data holds the json data sent by the api call
    data = request.data 
    
    print(data)
    
    # to access a specific field of a json file 
    print(data["name"])
    
    
    return Response()

@api_view(['POST'])
def addGps(request):
    
    # add to database
    # data = ItemSreialiser(data = request.data)
    # if(data.is_valid()):
    # data.save()

    data = request.data
    
    a = Animal.objects.create(id = data["id"], lat=data["Lat"], longitude=data["Long"])
    a.save()
    print(a)
    
    return Response()
    
    # lat = data["Lat"]
    # longitude = data["Long"]
    # id = data["id"]
    
    
    
    
    
    
    
    
    


# {
#     "name" : "hello"
# }

# {
# "name" : "hello",
# "place" : "margao"
# }