from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers import Employeemodel,Employeeserializer
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework import authentication,permissions


class Employeelistcreate(APIView):
    def get(self,request,*args,**kwargs):
        qs=Employeemodel.objects.all()
        serializer=Employeeserializer(qs,many=True)
        return Response(serializer.data)
    
    def post(self,request,*args,**kwargs):
        serializer=Employeeserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    
class Employeemixin(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        try:
            qs=Employeemodel.objects.get(id=id)
            serializer=Employeeserializer(qs,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
             return Response({"message":"id doesn't exist"}, status=status.HTTP_404_NOT_FOUND)
        
    def put(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Employeemodel.objects.get(id=id)
        serializer=Employeeserializer(data=request.data,instance=qs)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    

    def delete(self,request,*args,**kwargs):
         id=kwargs.get("pk")
         Employeemodel.objects.get(id=id).delete()
         return Response(status=status.HTTP_200_OK)
    

#####viewset ########

class EmployeeViewsetview(ViewSet):

########AUTHENTICATION AND PERMISSIONS ##########
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
 ##########################################################
 
    def list(self,request,*args,**kwargs):
        qs=Employeemodel.objects.all()
        serializer=Employeeserializer(qs,many=True)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    
    def create(self,request,*args,**kwargs):
        serializer=Employeeserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
        
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Employeemodel.objects.get(id=id)
        serializer=Employeeserializer(qs)
        return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    

    def update(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Employeemodel.objects.get(id=id)
        serializer=Employeeserializer(data=request.data,instance=qs)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)
        
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Employeemodel.objects.get(id=id).delete()
        return Response()
        


