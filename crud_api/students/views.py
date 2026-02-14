# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Student
from .serializers import StudentSerializer
from django.shortcuts import render, redirect


@api_view(['GET', 'POST'])
def student_list(request):

    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    if request.method == 'DELETE':
        student.delete()
        return Response({"message": "Student deleted"})

def student_ui_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

# def add_student_ui(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         course = request.POST['course']
#         Student.objects.create(name=name, email=email, course=course)
#         return redirect('student_ui_list')

#     return render(request, 'students/add.html')

def add_student_ui(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            course=request.POST['course']
        )
        return redirect('student_ui_list')

    return render(request, 'students/form.html', {'title': 'Add Student'})

def update_student_ui(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.course = request.POST['course']
        student.save()
        return redirect('student_ui_list')

    return render(request, 'students/form.html', {
        'title': 'Update Student',
        'student': student
    })


def delete_student_ui(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_ui_list')



