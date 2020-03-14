from django.urls import path
from my_form import views

urlpatterns = [
    path('',views.home, name = 'home-page'),
    path('client/', views.addclient, name = 'client-page'),
    path('create/', views.createclient, name = 'create-page'),
    path('detail/<int:pk>', views.client_details, name = 'detail-page'),

    
   
]
