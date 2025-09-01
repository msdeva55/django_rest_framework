from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student

class StudentAPI(APIView):

    def post(self, request):

        print(request.data)

        new_student = Student(name = request.data['name'],age = request.data['age'])
        
        new_student.save()

        return Response("New student created")