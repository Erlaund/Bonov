from django.urls import path 
from .views import * 

urlpatterns = [
	path('', Home.as_view(), name='home'),
	path('mail/<str:slug>/', GetMail.as_view(), name='mail'),
	path('mailform/', MailForm.as_view(), name='mailform'),

]


