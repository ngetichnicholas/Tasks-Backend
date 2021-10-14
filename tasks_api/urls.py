from django.urls import path
from .import views as api_views

urlpatterns = [ 
    path('',api_views.apiOverview,name="api-overview"),
    path('task-list',api_views.taskList,name="task-list"),

]