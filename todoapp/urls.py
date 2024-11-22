from django.urls import path
from . import views

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('tasklistview/',views.tasklistview.as_view(),name='tasklistview'),
    path('taskdetailview/<int:pk>/',views.taskdetailview.as_view(),name='taskdetailview'),
    path('taskupdateview/<int:pk>/',views.taskupdateview.as_view(),name='taskupdateview'),
    path('taskdeleteview/<int:pk>/',views.taskdeleteview.as_view(),name='taskdeleteview'),
    # path('details/',views.details,name='details'),

]