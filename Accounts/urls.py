from django.urls import path,include

from .views import login,signoff,signup

urlpatterns = [
    path('login/',login ,name='login'),
    path('signup/',signup,name='signup'),
    path('signoff/',signoff,name='signoff'),
]
