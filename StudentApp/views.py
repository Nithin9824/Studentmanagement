from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect


# Create your views here.
from StudentApp.models import City, Course, Student


def reg_fun(request):
    return render(request,'register.html',{'data':''})


def regdata_fun(request):
    user_name = request.POST['txtUserName']
    user_email = request.POST['txtUserEmail']
    user_password = request.POST['txtUserPassword']

    if User.objects.filter(Q(username=user_name) | Q(email=user_email)).exists():
        return render(request,'register.html',{'data':'Username or email already exists'})
    else:
        u1 = User.objects.create_superuser(username=user_name,email=user_email,password=user_password)
        u1.save()
        return redirect('log')


def log_fun(request):
    return render(request,'login.html',{'data':''})


def logdata_fun(request):
    user_name = request.POST['txtUserName']
    user_password = request.POST['txtUserPassword']
    user1 = authenticate(username=user_name,password=user_password)
    if user1 is not None:
        if user1.is_superuser:
            return render(request,'home.html')
        else:
            return render(request,'login.html',{'data':'User is not a superuser'})
    else:
        return render(request, 'login.html',{'data':'Enter proper username and password'})


def home_fun(request):
    return render(request,'home.html')


def addstudent_fun(request):
    city = City.objects.all()
    course = Course.objects.all()
    return render(request,'add_student.html',{'City_Data':city,'Course_Data':course})


def readdata_fun(request):
    s1 = Student()
    s1.Stud_Name = request.POST['txtName']
    s1.Stud_Age = request.POST['txtAge']
    s1.Stud_Phno = request.POST['txtPhno']
    s1.Stud_City = City.objects.get(City_Name = request.POST['ddlCity'])
    s1.Stud_Course = Course.objects.get(Course_Name=request.POST['ddlCourse'])
    s1.save()

    return redirect('add')


def display_fun(request):
    s1 = Student.objects.all()
    return render(request,'display_student.html',{'data':s1})


def update_fun(request,id):
    s1 = Student.objects.get(id=id)
    city = City.objects.all()
    course = Course.objects.all()

    if request.method == 'POST':
        s1.Stud_Name = request.POST['txtName']
        s1.Stud_Age = request.POST['txtAge']
        s1.Stud_Phno = request.POST['txtPhno']
        s1.Stud_City = City.objects.get(City_Name=request.POST['ddlCity'])
        s1.Stud_Course = Course.objects.get(Course_Name=request.POST['ddlCourse'])
        s1.save()
        return redirect('display')

    return render(request,'update.html',{'data':s1,'City_Data':city,'Course_Data':course})


def delete_fun(request,id):
    s1 = Student.objects.get(id=id)
    s1.delete()
    return redirect('display')


def log_out_fun(request):

    return redirect('log')