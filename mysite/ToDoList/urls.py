from django.urls import path

from . import views
app_name = 'ToDoList'
urlpatterns = [
    path("", views.index, name="index"),
    path('<int:pk>/complete/',views.complete,name = 'complete'),
    path('<int:pk>/delete',views.delete_todo,name= 'delete')
]