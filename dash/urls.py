from django.urls import path

from . import views


urlpatterns=[
	
	path('login/',views.loginpage, name="loginpage"),
	path('logout/',views.logoutuser, name="logoutpage"),
	path('Reset/',views.registrationpage, name="Resetpassword"),
	path('',views.homepage, name="homepage"),
	path('details/',views.persondetails, name ="details"),
	path('create/',views.createdetail, name ="create"),
	path('full-details/<str:pk>/',views.fulldetail, name ="full-details"),
	path('update-details/<str:pk>/',views.updatedetails, name ="update-details"),
	path('delete-details/<str:pk>/',views.deletedetails, name ="update-details"),
]