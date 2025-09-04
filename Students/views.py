from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.decorators import api_view

class StudentAPI(APIView):

    def get(self, request):

        all_students = Student.objects.all()

        student_data = Student_Serializer(all_students, many=True).data

        # student_list = []

        # for s in all_students:

        #     student_dict = {
        #         "id" : s.id,
        #         "name" : s.name,
        #         "age" : s.age
        #     }

        #     student_list.append(student_dict)

        return Response(student_data)

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

            task_data = Task_data_Serializer(all_task, many=True).data

            return Response(task_data)

        else:

            task = Task.objects.get(id=task_id)

            task_data = Task_Serializer(task).data

            return Response(task_data)

    # def get(self, request):

    #     all_task = Task.objects.all()

    #     task_data = Task_Serializer(all_task, many=True).data

    #     return Response(task_data)

    def post(self, request, task_id=None, *args, **kwargs):

        new_task = Task(student_reference_id = request.data['student_reference'], task_name=request.data['task_name'], description=request.data['description'])

        new_task.save()
        return Response("New Task Created")
        # new_task = Task_data_Serializer(data=request.data)

        # if new_task.is_valid():

        #     new_task.save()

        #     return Response("New Task Created")

        # else:

        #     return Response(new_task.errors, status=400)

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




    # def get(self, request, id=None):  

    #     if id == None:

    #         all_rank_sheets = RankSheet.objects.all()

    #         rank_data = RankSheet_Serializer(all_rank_sheets, many=True).data

    #         return Response(rank_data)

    #     else:

    #         rank = RankSheet.objects.get(id=id)

    #         rank_data = RankSheet_Serializer(rank).data

    #         return Response(rank_data)

    # def post(self,request):

    #     total_marks = request.data['tamil'] + request.data['english'] + request.data['maths'] + request.data['science'] + request.data['social_science']

    #     average_marks = total_marks / 5

    #     if (request.data['tamil'] >=35) and (request.data['english'] >=35) and (request.data['maths'] >=35) and (request.data['science'] >=35) and (request.data['social_science'] >=35):
            
    #         student_result = True

    #     else:

    #         student_result = False

    #     new_data = RankSheet(tamil = request.data['tamil'], english = request.data['english'], 
    #     maths = request.data['maths'], science = request.data['science'], social_science = request.data['social_science'],
    #     total = total_marks, average = average_marks,result = student_result)

    #     new_data.save()

    #     return Response("Rank sheet created successfully")


    # def patch(self,request,id):

    #     total_marks = request.data['tamil'] + request.data['english'] + request.data['maths'] + request.data['science'] + request.data['social_science']

    #     average_marks = total_marks / 5

    #     if (request.data['tamil'] >=35) and (request.data['english'] >=35) and (request.data['maths'] >=35) and (request.data['science'] >=35) and (request.data['social_science'] >=35):
            
    #         student_result = True

    #     else:

    #         student_result = False

    #     new_data.update(tamil = request.data['tamil'], english = request.data['english'], 
    #     maths = request.data['maths'], science = request.data['science'], social_science = request.data['social_science'],
    #     total = total_marks, average = average_marks,result = student_result)

    #     new_data.save()

    #     return Response("Rank sheet updated successfully")

    # def delete(self,request,id):

        rank = RankSheet.objects.get(id=id)

        rank.delete()

        return Response("Rank sheet deleted successfully")

#FBV
@api_view(['GET','POST'])
def task_list_create(request):

    if request.method == 'GET':

        all_task = Task.objects.all()

        task_data = Task_Serializer(all_task, many=True).data

        return Response(task_data)

    elif request.method == 'POST':

        new_task = Task_Serializer(data=request.data)

        if new_task.is_valid():

            new_task.save()

            return Response("New Task Created")

        else:

            return Response(new_task.errors, status=400)    

@api_view(['GET','PATCH','PUT','DELETE'])
def task_update_delete(request,id):

    task = Task.objects.get(id=id)

    if request.method == 'GET':

        task_data = Task_Serializer(task).data

        return Response(task_data)

    elif request.method == 'PATCH':

        update_task = Task_Serializer(task, data=request.data, partial=True)

        if update_task.is_valid():

            update_task.save()

            return Response("Task updated successfully")

        else:

            return Response(update_task.errors, status=400) 

    elif request.method == 'PUT':

        update_task = Task_Serializer(task, data=request.data)

        if update_task.is_valid():

            update_task.save()

            return Response("Task updated successfully")

        else:

            return Response(update_task.errors, status=400)

    elif request.method == 'DELETE':

        task.delete()

        return Response("Task deleted successfully")


