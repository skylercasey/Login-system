from django.urls import path
from .views import home,login_view,logout_view,signup_view

urlpatterns = [
    path('home/', home ,name='home'),
    path('logout/', logout_view,name='logout'),
    path('login/',login_view, name='login'),
    path('signup', signup_view,name='signup'),
    
]