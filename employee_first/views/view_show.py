from django.shortcuts import render,redirect
from employee_first.models import employee
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.


def show_data(request):
    all_data = employee.objects.all()
    contax = {"employee": all_data}
    return render(request, "Show_data.html", contax)


def welcome_func(request):
    print(request.method)
    if request.method == "POST":
        if not request.POST.get("eid"):

             emp_name=request.POST["ename"]
             emp_designation = request.POST["edis"]
             emp_salary = request.POST["esalary"]

             employee.objects.create(name=emp_name,designation=emp_designation,salary=emp_salary)
             return redirect("welcome")
        else:
            emp_id = request.POST.get("eid")
            data = employee.objects.get(id=emp_id )
            data.name = request.POST["ename"]
            data.designation = request.POST["edis"]
            data.salary = request.POST["esalary"]
            data.save()
            messages.success(request,"The data is edit succfully!!")
            return redirect("show")

    elif request.method == "GET":

        return render(request,"welcome.html")


def edit_data(request,eid):
    singal_data = employee.objects.get(id=eid)
    context = {'single_data' : singal_data}
    return render(request,"welcome.html",context)



def restore_data(request,eid):

    data = employee.objects.get(id=eid)
    if data.is_active == "N":
        data.is_active = "Y"
        data.save()
    return redirect("softdeletedata")














