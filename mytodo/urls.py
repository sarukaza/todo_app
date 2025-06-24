from django.urls import path
from mytodo import views as mytodo

urlpatterns = [
    path("", mytodo.index,name="index"),
    path("add/", mytodo.add,name="add"), # あとで使う
    path("update_task_complete/", mytodo.update_task_complete, name="update_task_complete"),
    path("delete_task/", mytodo.delete_task, name="delete_task"),
    path("edit_task/<int:task_id>/", mytodo.edit_task, name="edit_task"),
]