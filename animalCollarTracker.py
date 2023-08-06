# this code is to be run on the collars of the stray animals 
# it updates the gps data on the main server at a set interval
# of 10 minutes  

import requests 
import time

# Id derermined during maufacturing of device 
ID = "o1u24jb4123"


apiEndpoint = "http://127.0.0.1:8000/updateGps/"

# dummy function to return current gps coordinates 
def getGps():
    lat = 123.534
    longitude = 4321.342
    return lat, longitude 


while( True):
    lat, longitude = getGps()

    data = {
        "id" : ID,
        "Lat" : lat,
        "Long" : longitude
    }

    requests.post(url=apiEndpoint, data=data)
    
    # update every 10 minutes 
    time.sleep(600)