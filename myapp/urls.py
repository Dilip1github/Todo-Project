from django.urls import path
from . import views

urlpatterns = [
    path('create_task',views.create_task,name='create_task'),
    path('task_form',views.task_form,name='task_form'),
    path('',views.get_task,name='get_task'),
    path('delete/<rid>',views.delete,name='delete'),
    path('edit/<rid>',views.edit,name='edit'),
]