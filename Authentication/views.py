from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from django.contrib.auth import authenticate

class UserView(APIView):

    def post(self, request):

        new_user = User(username = request.data['username'], is_superuser = request.data['is_superuser'])
        
        new_user.set_password(request.data['password'])
        
        new_user.save()
        
        return Response("New User Registered")
    
class UserLoginView(APIView):

    def post(self, request):

        user_verification = authenticate(username = request.data['username'], password = request.data['password'])

        if user_verification == None:
            return Response("Invalid Credentials", status=401)
        else:   
            return Response("User logged in")