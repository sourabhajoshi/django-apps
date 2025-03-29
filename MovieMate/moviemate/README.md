

DRF : Django Rest Framework
pip install djangorestframework

add into settings.py of project
[
    ....,
    'rest_framework',
]

Serialization vs D-Serialization
Serialization convert complex datatype (class_name.object.all()) into python native data type. Than render into JSON Data
De-Serialization convert python native datatype into complex datatype.


=> Type of serializers : srilaizrers.Serializer and serializers.ModelSerializers
Note : it is not officialy devided

=> Type of views : class bassed and functional bassed

    class bassed view : we use ApiView class. 
    import APIView from rest_framework.views and use it in class 
    class ListUser(APIView):

    functional bassed views : It provide @api_view() 
    import res_framework.decorators import api_view
    @api_view() 
    def hello_world(request):
        //statements

=> Working with API : we can test our api or access api using these three
    DRF browsable API
    Postman
    HTTPie (Not recomanded)


=> status code : https://www.django-rest-framework.org/api-guide/status-codes/
    we can add status code for ERROR, SUCCESS and aso for CRUD

=> APIView Class

=> Validations : API guide > serializers > validation : https://www.django-rest-framework.org/api-guide/serializers/#validation
   3 types : field level (only for one field), object level (for complete object, .object.all() level), validators

=> Core arguments : serializer field > core arguments : https://www.django-rest-framework.org/api-guide/fields/#core-arguments

=> ModelSerializer : https://www.django-rest-framework.org/api-guide/serializers/#modelserializer