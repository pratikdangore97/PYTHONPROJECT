"""employee_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employee_first import views
from django.views.generic.base import TemplateView
urlpatterns = [
    path('', views.welcome_func, name='home'),
    path('admin/', admin.site.urls),
    path('welcome/',views.welcome_func, name="welcome"),
    path('show_data/', views.show_data,name="show"),
    path('Edit/<int:eid>',views.edit_data,name="edit"),
    path('Delete/<int:eid>',views.delete_data,name="delete"),
    path('soft_delete/<int:eid>',views.soft_delete,name= "softdelete"),
    path('delete_all',views.delete_data,name="deleteall"),
    path('soft_deleted_data',views.soft_deleted_data,name="softdeletedata"),
    path('Restore/<int:eid>',views.restore_data,name="restore"),
    path('Export',views.export_csv_file,name="export"),
    path('Import',views.import_csv_data,name="import"),


]
