#Running
##Frontend
```console
cd animals
npm start
```
This starts the React app that creates a map at localhost:3000 with points at the locations of the animals
##Backend
```console
python manage.py runserver 
python animalCollarTracker.py
```
This starts the Django backend which handles the database. 
Adding new entries is handled by the collar on the animal itself, and so is updating the current gps coordinates 
at a regular time interval.

To access the current animal details in the database, 
use :
http://127.0.0.1:8000/get/


API data format for location of an animal : 
{
    "id" : " xxxxxx",
    "Lat" : " _value_ ",
    "Long" : " _value_ "
}

