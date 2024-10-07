from django.shortcuts import render

from django.views.generic import View

from EMP_app.forms import Employeeform,Employeemodelform

from EMP_app.models import Employeemodel


class Register(View):

    def get(self,request):

        form=Employeeform()

        return render (request,"index.html",{"form":form})
    
    def post(self,request):

        form=Employeemodelform(request.POST)
        
        if form.is_valid():

            print(form.cleaned_data)

            print(form.cleaned_data.get("employee_name"))

            Employeemodel.objects.create(**form.cleaned_data)
            
            return render(request,"index.html")
        
        else:

            return render(request,"index.html")
        


class Employeemodelview(View):

    def get(self,request):

        form=Employeemodelform()

        return render (request,"index2.html",{"form":form})
    
    def post(self,request):

        form=Employeemodelform(request.POST)
        
        if form.is_valid():

            form.save()
            
        return render(request,"index2.html")
    

        
          ########    READ     ##########

class Employees(View):
    
    def get(self,request):

        data=Employeemodel.objects.all()

        return render(request,"index3.html",{"data":data})
    


####### DETAIL ############

class Employeedetail(View):
    
    def get(self,request,**kwargs):

        id=kwargs.get("pk")

        data=Employeemodel.objects.get(id=id)

        print(data)

        return render(request,"index4.html",{"data":data})
    

    ##### DELETE #######


class EmployeeDelete(View):

    def get(self,request,**kwargs):

        id=kwargs.get("pk")

        Employeemodel.objects.get(id=id).delete()

        print("deleted successfully")

        return render(request,"index.html")
    

###### UPDATE ###########

class EmployeeUpdate(View):
    
    def get(self,request,**kwargs):

        id=kwargs.get("pk")

        data=Employeemodel.objects.get(id=id)

        form=Employeemodelform(instance=data)

        return render(request,"index5.html",{"form":form})
    
    def post(self,request,**kwargs):

        id=kwargs.get("pk")

        data=Employeemodel.objects.get(id=id)

        form=Employeemodelform(request.POST,instance=data)
        
        if form.is_valid():

            form.save()

            print("update successfully")
            
        return render(request,"index5.html",{"form":form})