from django.urls import path
from .views import *

urlpatterns = [
    path('admin-login/', AdminLoginView.as_view(), name='admin-login'),
    path('uidesigners/', UIDesignersAPIView.as_view(), name='uidesigners-list-create'),   
    path('uidesigners/<int:pk>/', UIDesignersDetailAPIView.as_view(), name='uidesigners-detail'),   
    path('developers/', DevelopersAPIView.as_view(), name='uidesigners-list-create'),   
    path('developers/<int:pk>/', DevelopersDetailAPIView.as_view(), name='uidesigners-detail'), 
    path('Socialmedia/',SocialMediaAPIView.as_view(), name='uidesigners-list-create'),   
    path('Socialmedia/<int:pk>/', SocialMediaDetailAPIView.as_view(), name='uidesigners-detail'),
    path('account/',AccountAPIView.as_view(), name='uidesigners-list-create'),   
    path('account/<int:pk>/', AccountDetailAPIView.as_view(), name='uidesigners-detail'), 
    path('client/',ClientAPIView.as_view(), name='uidesigners-list-create'),   
    path('client/<int:pk>/', ClientDetailAPIView.as_view(), name='uidesigners-detail'),  
    path('project/',ProjectsAPIView.as_view(), name='uidesigners-list-create'),   
    path('project/<int:pk>/', ProjectsDetailAPIView.as_view(), name='uidesigners-detail'),  
    path('invoice/',InvoiceAPIView.as_view(), name='uidesigners-list-create'),   
    path('invoice/<int:pk>/', InvoiceDetailAPIView.as_view(), name='uidesigners-detail'),  
    
]
