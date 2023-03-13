from rest_framework import serializers
from .models import MyDesignItem

# class MyDesignItemSerializer(serializers.Serializer) :
#     id = serializers.IntegerField() #PK
#     design_name = serializers.CharField(max_length=255)
#     design_code = serializers.CharField(max_length=18)
#     designer = serializers.CharField()
#     img = serializers.CharField()

#     def create(self, validated_data) :
#         return MyDesignItem.objects.create(**validated_data)

#     def update(self, instance, validated_data) :
#         #instance.id = validated_data.get('id', instance.id)
#         instance.design_name = validated_data.get('design_name', instance.design_name)
#         instance.design_code = validated_data.get('design_code', instance.design_code)
#         instance.designer = validated_data.get('designer', instance.designer)
#         instance.img = validated_data.get('img', instance.img)
#         instance.save()
#         return instance


class MyDesignItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyDesignItem
        fields = '__all__'