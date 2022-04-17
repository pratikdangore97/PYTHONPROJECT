from employee_first.models import  employee
from django.shortcuts import render,redirect
from django.contrib import messages

def soft_delete(request, eid):
    emp_id = employee.objects.get(id=eid)
    print(emp_id)
    active = employee.objects.get(name=emp_id)

    if active.is_active == "Y":
        active.is_active = "N"
        active.save()
    else:
        active.is_active = "Y"
        active.save()
    return redirect("show")


def delete_all(request):
    data = employee.objects.all()
    data.delete()
    data.save()
    return redirect("show")


def soft_deleted_data(request):
    data = employee.objects.filter(is_active="N")
    con = {'softdeletebook': data}
    return render(request, "soft_deleted_data.html", con)

def delete_data(request,eid):
    emp_data = employee.objects.get(id=eid)
    emp_data.delete()
    messages.info(request,"The data delete succfully!!")
    return redirect("show")