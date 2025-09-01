from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student

class StudentAPI(APIView):

    def get(self, request):

        all_students = Student.objects.all()

        student_list = []

        for s in all_students:

            student_dict = {
                "id" : s.id,
                "name" : s.name,
                "age" : s.age
            }

            student_list.append(student_dict)

        return Response(student_list)

    def post(self, request):

        # print(request.data)

        new_student = Student(name = request.data['name'],age = request.data['age'])
        
        new_student.save()

        return Response("New student created")

    def put(self, request, student_id):

        # print(student_id, "student_id")

        student_data = Student.objects.filter(id = student_id)

        # print(request.data)

        student_data.update(name = request.data['name'],age = request.data['age'])

        return Response("Student Data updated")

    def delete(self, request, student_id):

        student_data = Student.objects.get(id = student_id)

        student_data.delete()

        return Response("Student data deleted")