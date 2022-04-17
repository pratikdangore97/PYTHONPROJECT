from employee_first.models import employee
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect,reverse
from django.contrib import messages
import csv


def export_csv_file(request):
    all_csv_data = employee.objects.filter(is_active = "Y")
    response = HttpResponse(content_type="text/csv")
    csv_writer=csv.writer(response)
    csv_writer.writerow(["ID","Name","Designation","salary"])

    for emp in all_csv_data.values_list('id','name','designation','salary','is_active'):
        csv_writer.writerow(emp)

    response['Content-Disposition'] = 'attachment; filename=Employee_Data.csv'
    return response


# def import_csv_data(request):
#     return render(request, "import_csv.html")


def import_csv_data(request):

    if  request.method == "GET":
        return render(request, "import_csv.html")

    if request.method == "POST":
        csv_file = request.FILES["csv_file"]

        if not csv_file.name.endswith(".csv"):
            messages.warning(request,'Only CSV file needed!!')
            return HttpResponseRedirect("Import")
        else:
            try:
                file_data = csv_file.read().decode("utf-8")
                csv_data = file_data.split("\n")

                for x in csv_data:
                    field = x.split(",")
                    #print(field[0],field[1])
                    data = employee.objects.create(name=field[0],designation=field[1],salary=field[2],is_active=field[3])
                    data.save()
                return redirect("show")
            except Exception as e:
                print("issue in file ..please check",e)
                return redirect("show")






