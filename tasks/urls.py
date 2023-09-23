from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('create', views.create, name='create'),
    path('<int:pk>/update', views.UpdateTask.as_view(), name='update'),
]