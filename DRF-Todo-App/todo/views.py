from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

# Create your views here.

#listout all the tasks
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class TaskRetriveUpdateDeleteView(generics.RetrieveUpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
