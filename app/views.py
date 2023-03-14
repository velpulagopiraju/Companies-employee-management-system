from django.shortcuts import render
from rest_framework import viewsets
from app.models import company,employee
from app.serializers import company_serializer,employee_serilalizer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.


class companyview(viewsets.ModelViewSet):
    queryset = company.objects.all()
    serializer_class = company_serializer

    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            comp = company.objects.get(pk=pk)
            emps = employee.objects.filter(company=comp)
            emp_serializer = employee_serilalizer(emps,many=True,context = {'request':request})
            return Response(emp_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'company not exist'
            })

        



class employeeview(viewsets.ModelViewSet):
    queryset = employee.objects.all()
    serializer_class = employee_serilalizer