#----------- Moved this file into api/views.py ---------------

# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse

# # function bassed view
# def movie_list(request):
#     movies = Movie.objects.all()
#     # movies_list = list(movies.values())  # Convert QuerySet to a list of dictionaries
    
#     # send data as dict {}
#     data = {'movies' : list(movies.values())} # {"movies": [{"id": 1, "name": "python", "descrption": "Som descriptions", "active": true}, {"id": 2, "name": "javascript", "descrption": "Som descriptions", "active": true}]}
#     return JsonResponse(data, safe=False)


# # to get perticular movie based on id : we need to set the url also go to urls.py and set url
# def movie_details(request, pk):
#     # pk : primery key
#     movie = Movie.objects.get(pk=pk) # do not use .all, use .get() we are filtering here
#     data = {
#         'name' : movie.name,
#         'descrption' : movie.descrption,
#         'active' : movie.active
        
#     }
#     return JsonResponse(data, safe=False) #{"name": "python", "descrption": "Som descriptions", "active": true}
