
from django.urls import path

from home import views

app_name="home"

urlpatterns = [

    path('',views.home, name="homepage"),
    path('services',views.services,name='servicespage'),
    path('works', views.works, name='workspage'),
    path('contact', views.contact, name='contactpage'),
    path('add',views.add, name="addpage"),
    path('view',views.view, name="viewdata")

]