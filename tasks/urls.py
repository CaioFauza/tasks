from django.urls import path

from . import views

urlpatterns = [
    path('', views.task, name='get__create_tasks'),
    path('<int:id>', views.task, name='update__delete_task')
]
