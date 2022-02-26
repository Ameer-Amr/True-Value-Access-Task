from django.urls import path
from django.conf.urls import include
from .views import UserDetailView, UserRegisterView

urlpatterns = [

   path('api/users',UserRegisterView.as_view(),name='register'),
   path('api/users/<int:pk>',UserDetailView.as_view(),name='register'),
]
