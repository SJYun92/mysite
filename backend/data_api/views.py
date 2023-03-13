from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MyDesignItem
from .serializers import MyDesignItemSerializer


# Create your views here.

class MyDesignItemView(APIView) :
    def get(self, request, pk=None) :
        if pk:
            data = MyDesignItem.objects.get(pk=pk)
            serializer = MyDesignItemSerializer(data)
        else :
            data = MyDesignItem.objects.all()
            serializer = MyDesignItemSerializer(data, many=True)
        return Response({"result": serializer.data})

    def post(self, request) :
        item = request.data
        serializer = MyDesignItemSerializer(data=item)
        if serializer.is_valid(raise_exception=True) :
            item_saved = serializer.save()
        return Response({"result" : f"My Design Item {item_saved.design_name}"})

    def put(self, request, pk) :
        saved_item = get_object_or_404(MyDesignItem.objects.all(), pk=pk)
        data = request.data
        serializer = MyDesignItemSerializer(instance=saved_item, data=data, partial=True)   #partial means not all fields are required 
        
        #The .is_valid() method takes an optional raise_exception flag that will cause it to raise a serializers.ValidationError exception if there are validation errors.
        if serializer.is_valid(raise_exception=True) :
            saved_item = serializer.save()

        return Response({"result" : f"{saved_item.design_name} updated"})


    def delete(self, request, pk):
        item = get_object_or_404(MyDesignItem.objects.all(), pk=pk)
        item.delete()
        return Response({"result" : f"MyDesignItem id {pk} deleted"}, status=204)