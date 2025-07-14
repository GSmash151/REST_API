# from django.shortcuts import render
# from django.http import JsonResponse
from employees.models import Employee
from students.models import Student
from .serializers import EmployeeSerializers, StudentSerializers
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins, generics


@api_view(["GET", "POST"])
# Create your views here.
def studentsView(request):
    if request.method == "GET":
        # Get all the data from the Students table
        students = Student.objects.all()
        serializer = StudentSerializers(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def studentDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StudentSerializers(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class Employees(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializers(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = EmployeeSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class EmployeesDetails(APIView):
#     def get_object(self, pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404

#     def get(self,request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializers(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializers(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class Employees(
    mixins.ListModelMixin, 
    mixins.CreateModelMixin, 
    generics.GenericAPIView
):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class EmployeesDetails(generics.GenericAPIView):
    pass


# ----------------------------------------- ( AI ) -------------------------------------#
# class StandardResultsSetPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     max_page_size = 100


# @api_view(['GET', 'POST'])
# def studentsView(request):
#     if request.method == 'GET':
#         students = Student.objects.all()
#         paginator = StandardResultsSetPagination()
#         result_page = paginator.paginate_queryset(students, request)
#         serializer = StudentSerializers(result_page, many=True)
#         return paginator.get_paginated_response(serializer.data)

#     elif request.method == 'POST':
#         serializer = StudentSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "PUT", "DELETE"])
# def studentDetailView(request, pk):
#     if not pk.isdigit():
#         return Response({"error": "Invalid primary key"}, status=status.HTTP_400_BAD_REQUEST)

#     try:
#         student = Student.objects.get(pk=pk)
#     except Student.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = StudentSerializers(student)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     elif request.method == "PUT":
#         serializer = StudentSerializers(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class Employees(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializers(employees, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializer = EmployeeSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class EmployeesDetails(APIView):
#     def get_object(self, pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404("Employee not found")

#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializers(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializers(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
