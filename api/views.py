from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def getData(request):
    # sample api json to return 
    person = {'name' : 'Foo', 'address' : 'bar'}
    return Response(person)