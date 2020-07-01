from django.contrib.auth.models import User, Group
from rest_framework import serializers
from push_api.models import fooddata
import json
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = fooddata
        fields = ['date', 'name', 'price', 'img_url', 'content']