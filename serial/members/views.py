'''from members.models import Reg
from members.serializers import RegSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class RegList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        r1 = Reg.objects.all()
        serializer = RegSerializer(r1, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RegSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class RegDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Reg.objects.get(pk=pk)
        except Reg.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        r1 = self.get_object(pk)
        serializer = RegSerializer(r1)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        r1 = self.get_object(pk)
        serializer = RegSerializer(r1, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''
         
'''from members.models import Reg
from members.serializers import RegSerializer
from rest_framework import mixins
from rest_framework import generics

class RegList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Reg.objects.all()
    serializer_class = RegSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        
        
class RegDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Reg.objects.all()
    serializer_class = RegSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)'''
    
    
'''from members.models import Reg
from members.serializers import RegSerializer
from rest_framework import generics


class RegList(generics.ListCreateAPIView):
    queryset = Reg.objects.all()
    serializer_class = RegSerializer
    
class RegDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reg.objects.all()
    serializer_class = RegSerializer'''
    
from members.models import Reg
from django.shortcuts import get_object_or_404
from members.serializers import RegSerializer
from rest_framework import viewsets
from rest_framework.response import Response

'''class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Reg.objects.all()
        serializer = RegSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Reg.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = RegSerializer(user)
        return Response(serializer.data)'''
        
class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances."""
    queryset = Reg.objects.all()
    serializer_class = RegSerializer
    
    
    
    
    
    
    
    