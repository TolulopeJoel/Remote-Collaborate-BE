from rest_framework import generics

from accounts.mixins import UserTeamQueryset

from .models import Task
from .serializers import TaskSerializer


class TaskList(UserTeamQueryset, generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    # return tasks for all team user is in.
    def get_queryset(self):
        queryset = super().get_queryset()
        user_queryset = []
        
        for team in queryset:
            tasks = team.tasks.all()
            for task in tasks:
                user_queryset.append(task)
        
        return user_queryset


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# class TaskViewset(UserTeamQueryset, viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
    
#     # return tasks for all team user is in.
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         user_queryset = []
        
#         for team in queryset:
#             tasks = team.tasks.all()
#             for task in tasks:
#                 user_queryset.append(task)
        
#         return user_queryset

# # A JSON representation of tasks to display tasks on calendar
# def task_data(request):
#     tasks = Task.objects.all()
#     task_list = []

#     for task in tasks:

#         # task status colors
#         color = ''
#         if task.status == 'in-progress':
#             color = '#007bff'
#         elif task.status == 'not-started':
#             color = '#f44336'
#         elif task.status == 'in-review':
#             color = '#ffc107'
#         elif task.status == 'suspended':
#             color = '#6c757d'
#         elif task.status == 'completed':
#             color = '#28a745'

#         task_list.append({
#             'title': task.name,
#             'start': task.start_date,
#             'end': task.due_date,
#             'color': color,
#         })
#     return JsonResponse(task_list, safe=False)


# def calendar(request):
#     return render(request, 'calendar.html')
