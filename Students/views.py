from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student, Task
from .serializers import Task_Serializer

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

class TaskView(APIView):

    def get(self, request, task_id=None):

        if task_id == None:

            all_task = Task.objects.all()

            task_data = Task_Serializer(all_task, many=True).data

            return Response(task_data)

        else:

            task = Task.objects.get(id=task_id)

            task_data = Task_Serializer(task).data

            return Response(task_data)

    # def get(self, request):

    #     all_task = Task.objects.all()

    #     task_data = Task_Serializer(all_task, many=True).data

    #     return Response(task_data)

    def post(self, request):

        new_task = Task_Serializer(data=request.data)

        if new_task.is_valid():

            new_task.save()

            return Response("New Task Created")

        else:

            return Response(new_task.errors, status=400)

    def patch(self, request, task_id):
        
        task = Task.objects.get(id=task_id)

        update_task = Task_Serializer(task, data=request.data, partial=True)

        if update_task.is_valid():

            update_task.save()

            return Response("Task updated successfully")

        else:

            return Response(update_task.errors, status=400) 


    def put(self, request, task_id):

    
        task = Task.objects.get(id=task_id)

        update_task = Task_Serializer(task, data=request.data, partial=True)

        if update_task.is_valid():

            update_task.save()

            return Response("Task updated successfully")
                
        else:

            return Response(update_task.errors, status=400)   

    def delete(self, request, task_id):


        task = Task.objects.get(id=task_id)

        task.delete()

        return Response("Task deleted successfully")