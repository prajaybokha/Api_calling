from rest_framework import serializers
from members.models import Reg


class RegSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Reg
        fields= "__all__"
         