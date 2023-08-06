from django.db import models

# database stuff 
# add whatever here , prefferably json based 




# creating a model entry 
class Animal(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    lat = models.FloatField(default = 0)
    longitude = models.FloatField(default = 0)
    
    