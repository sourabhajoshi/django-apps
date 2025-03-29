# =========== CLASS BASED VIEW =================
from rest_framework.response import Response
from rest_framework.views import APIView
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework import status

# class based function
class MovieListAV(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class MovieDetailAV(APIView):
    def get(self, request, pk):
        try:  
            movies = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'ERROR' : 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = MovieSerializer(movies) # here not requered to write many=True, bcz we are searvhing direct pk. Only one value so
        
        #status code is 200 bydefault
        return Response(serializer.data)
    
    def put(self, request, pk):
        movies = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movies, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        movies = Movie.objects.get(pk=pk)
        movies.delete()
        # once after delete we need to send user message. (status code) : https://www.django-rest-framework.org/api-guide/status-codes/
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
        
        






# ============ FUNCTION BASED VIEW ================

# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from watchlist_app.models import Movie
# from watchlist_app.api.serializers import MovieSerializer
# from rest_framework import status


# # function bassed view
# @api_view(['GET', 'POST'])
# def movie_list(request):
#    # get complex data
#    if request.method == 'GET':
#        movies = Movie.objects.all()
#        serializer = MovieSerializer(movies, many=True) #when it need to visit multiple queryset we should write many=True
#        return Response(serializer.data)
   
#    if request.method == 'POST':
#        serializer = MovieSerializer(data = request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        else:
#            return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
#     if request.method == 'GET':
#         try:  
#             movies = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'ERROR' : 'Movie Not Found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movies) # here not requered to write many=True, bcz we are searvhing direct pk. Only one value so
        
#         #status code is 200 bydefault
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         # which obj we are going to select
#         movies = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movies, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        
#     if request.method == 'DELETE':
#         movies = Movie.objects.get(pk=pk)
#         movies.delete()
#         # once after delete we need to send user message. (status code) : https://www.django-rest-framework.org/api-guide/status-codes/
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
   
