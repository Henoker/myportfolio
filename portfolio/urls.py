from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('<slug>/',views.detail_blog_view, name='detail'),
     
    
    

]