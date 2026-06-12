from rest_framework.views import APIView
from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from .models import Course, Student

class CourseApiView(APIView):
    def get(self, request, pk: int = None):
        if not pk:
            courses = Course.objects.all()
            courses_list = []
            for course in courses:
                courses_list.append(
                    {
                        'id': course.pk,
                        'name': course.name
                    }
                )

            return Response(courses_list)
        else:
            course = Course.objects.get(pk=pk)
            return Response(model_to_dict(course))

    def post(self, request:Request, pk: int = None):
        if not pk:
            name = request.data.get("name", None)
            if name:
                course = Course.objects.create(name=name)
                return Response(model_to_dict(course), status=status.HTTP_201_CREATED)
            return Response({"message": "Xato!!!"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "Method not allowed!"}, 
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)
class StudentApiView(APIView):
    def get(self, request, pk: int = None):
        if not pk:
            students = Student.objects.all()
            students_list = []
            for student in students:
                students_list.append(
                    {
                        'id': student.pk,
                        'name': student.name,
                        'age': student.age,
                        'hudud': student.hudud,
                        'category_id': student.category.id

                    }
                )

            return Response(students_list)
        else:
            student = Student.objects.get(pk=pk)
            return Response(model_to_dict(student))

    def post(self, request:Request, pk: int = None):
        if not pk:
            name = request.data.get("name", None)
            age = request.data.get("age", None)
            hudud = request.data.get("hudud", None)
            category_id = request.data.get("category_id", None)



            if name and age and hudud and category_id:
                student = Student.objects.create(**request.data)
                return Response(model_to_dict(student), status=status.HTTP_201_CREATED)
            return Response({"message": "Xato!!!"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "Method not allowed!"}, 
                            status=status.HTTP_405_METHOD_NOT_ALLOWED)

