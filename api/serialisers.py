from rest_framework import serializers
from base.models import Animal

class ItemSreialiser(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'
        