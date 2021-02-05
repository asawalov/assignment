
from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('adminuser/',views.adminuser,name='adminuser'),
    path('annoymous/',views.annoymous,name='annoymous'),
    path('adminuser/createuser/',views.createuser,name='createuser'),
    # path('adminuser/createadminuser/',views.createadminuser,name='createadminuser'),
    # path('adminuser/createannoymoususer/',views.createannoymoususer,name='createannoymoususer'),
    path('adminuser/updateuser/<str:pk>/',views.updateuser,name='updateuser'),
    path('adminuser/deleteuser/<str:pk>/',views.deleteuser,name='deleteuser'),
    path('login/',views.loginPage,name='login'),
    path('register/',views.register,name='register'),
    path('logout/', views.logoutUser, name="logout"),

]
