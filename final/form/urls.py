
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('adminuser/',views.adminuser,name='adminuser'),
    path('annoymous/',views.annoymous,name='annoymous'),
    path('adminuser/createuser/',views.createuser,name='createuser'),
    path('adminuser/updateuser/<str:pk>/',views.updateuser,name='updateuser'),
    path('adminuser/deleteuser/<str:pk>/',views.deleteuser,name='deleteuser'),

]
