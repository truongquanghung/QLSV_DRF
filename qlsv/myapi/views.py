from django.shortcuts import render, redirect
from rest_framework.response import Response
from .models import student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view 
from django.views import View
from path import path

class Main(View):
    def get(self, request):
        Students = student.objects.all()
        serializer = StudentSerializer(Students, many=True)
        khoa = []
        for x in serializer.data:
            if x['faculty'] in khoa :
                continue
            khoa.append(x['faculty'])
        # print(khoa)
        context = {
            'data': serializer.data,
            'khoa': khoa,
        }
        return render(request, path.main, context)

class Search(View):
    def post(self, request):
        if request.POST.get('faculty')=='null':
            return redirect('/')
        else:
            Students = student.objects.filter(faculty=request.POST.get('faculty'))
        serializer = StudentSerializer(Students, many=True)
        khoa = []
        for x in serializer.data:
            if x['faculty'] in khoa :
                continue
            khoa.append(x['faculty'])
        # print(khoa)
        context = {
            'data': serializer.data,
            'khoa': khoa,
        }
        return render(request, path.main, context)
# Class-based view
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import permissions
from .permissions import IsAdminOrReadOnly

class StudentListView(generics.GenericAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]

    
    def get(self, request):
        Students = student.objects.all()
        serializer = StudentSerializer(Students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

class StudentDetailView(generics.GenericAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminOrReadOnly]
    success_url = '/'

    def get(self, request, pk):
        try:
            Students = student.objects.get(id=pk)
            serializer = StudentSerializer(Students, many=False)
        except:
            return Response("Not found")
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            Student = student.objects.get(id=pk)
            serializer = StudentSerializer(Student, data=request.data)
            if serializer.is_valid():
                serializer.save()
        except:
            return Response("Not found")
        return Response(serializer.data)

    def delete(slef, request, pk):
        try:
            Student = student.objects.get(id=pk)
            Student.delete()
        except:
            return Response("Not found")
        return Response("Deleted")

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .permissions import CustomPermission

class Create(CustomPermission,CreateView):
    model = student
    fields = ['mssv', 'name', 'sex', 'faculty']
    template_name = 'home/create.html'
    success_url = '/'

class Update(CustomPermission,UpdateView):
    model = student
    fields = ['mssv', 'name', 'sex', 'faculty']
    template_name = 'home/update.html'
    success_url = '/'

class Delete(CustomPermission,DeleteView):
    model = student
    template_name = 'home/delete.html'
    success_url = '/'