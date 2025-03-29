from rest_framework import serializers
from watchlist_app.models import Movie

# =========================== TYPE : serializers.ModelSerializer ==================================


# serializers.ModelSerializer also contain everything CRUD
class MovieSerializer(serializers.ModelSerializer):
    
    #custom serializer fields : we can add one more field ex : len_name
    len_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Movie
        fields = '__all__'
        
        # we can display what and all fields we want to show
        #fields = ["id", "name", "descrption"] # now active field wont visible
        
        # one more method to exclude fields
        # exclude = ["active"]
        
    def get_len_name(self, object):
        length = len(object.name)
        return length
        
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        else:
            return value
        
    def validate(self, data):
        if data['name'] == data['descrption']:
            raise serializers.ValidationError("Title and descrption should be diffrent")
        else:
            return data



# =========================== TYPE : serializers.Serializer ==================================
# def name_length(value):
#     if len(value) < 2 :
#         raise serializers.ValidationError("Name is too short")
    

# # we have two types of serializers, here i used serializers.Serializer
# class MovieSerializer(serializers.Serializer):
    
#     # this below used only for get request
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(validators = [name_length])
#     descrption = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     # instance ; old value and validate_data : new value
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.descrption = validated_data.get('descrption', instance.descrption)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     # field level validation : fun name should be like below as per documentation
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short")
#         else:
#             return value
        
#     # Object level validation : fun name should be as like doc
#     def validate(self, data):
#         if data['name'] == data['descrption']:
#             raise serializers.ValidationError("Title and descrption should be diffrent")
#         else:
#             return data
        
#     # validator : core arg passed to current field