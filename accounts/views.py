from django.shortcuts import render
from rest_framework import generics
from .models import accounts
from .serializers import UserDetails, UserRegister
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter,OrderingFilter

# Create your views here.
class UserRegisterView(generics.ListCreateAPIView):
    serializer_class = UserRegister
    queryset = accounts.objects.all()
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['first_name', 'last_name']
    
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserRegister(user,context=self.get_serializer_context()).data,
            "message": "Registered Successfully.",
        },status=status.HTTP_201_CREATED)
        
        
    # def get(self,request):
    #     queryset = self.get_queryset()
    #     serializer = UserRegister(queryset,many=True)
    #     return Response(serializer.data,status=status.HTTP_200_OK)
    
    
class UserDetailView(APIView):
    def get(self, request,pk):
        id = pk
        user = accounts.objects.get(pk=id)
        serializer = UserDetails(user)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self, request,pk):
        id = pk
        user = accounts.objects.get(pk=id)
        serializer = UserDetails(user,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,pk):   
        id = pk
        user = accounts.objects.get(pk=id)
        user.delete()
        return Response({'Message':"User deleted successfully"},status=status.HTTP_200_OK)       
        
    
    
    