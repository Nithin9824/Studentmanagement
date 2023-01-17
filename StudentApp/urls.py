from django.urls import path

from StudentApp import views

urlpatterns = [
    path('',views.log_fun,name='log'),
    path('logdata',views.logdata_fun),#it will read data and verify if superuser and redirect to
    path('reg',views.reg_fun,name='reg'),#it will open register.html page
    path('regdata',views.regdata_fun),#it will create superuser account

    path('home',views.home_fun,name='home'),#it will redirect to home.html

    path('add',views.addstudent_fun,name='add'),#it will redirect to add_student.html
    path('readdata',views.readdata_fun),

    path('display',views.display_fun,name='display'),

    path('update/<int:id>',views.update_fun,name='up'),#it will update student data
    path('delete/<int:id>',views.delete_fun,name='del'),#it will delete record from student table
    path('log_out',views.log_out_fun,name='log_out')


]