from django.shortcuts import render,redirect
from .models import Course,Student

# Create your views here.
def home(request):
    return render(request,'home.html')

def addcourse(request):
    return render(request,'addcourses.html')

def addcoursedetails(request):
    if request.method == 'POST':
        cname = request.POST.get('cname')
        cfee=request.POST.get('cfee')
        cobj=Course(coursename=cname,coursefee=cfee)
        cobj.save()
        return redirect('addcourse')
    return render(request,'addcourses.html')


def addstudent(request):
    course=Course.objects.all()
    return render(request,'addstudent.html',{'course':course})

def addstudentdetails(request):
    if request.method == 'POST':
        sname=request.POST.get('sname')
        saddress=request.POST.get('saddress')
        sage=request.POST.get('sage')
        date=request.POST.get('date')
        sel=request.POST.get('sel')
        course=Course.objects.get(id=sel)
        obj=Student(studentname=sname,address=saddress,age=sage,date=date,course=course)
        obj.save()
        return redirect('studentdetails')
    return render(request,'addstudent.html')

def studentdetails(request):
    stu=Student.objects.all()
    return render(request,'showdetails.html',{'student':stu})

def editpage(request,id):
    c=Course.objects.all()
    s=Student.objects.get(id=id)
    return render(request,'editpage.html',{'student':s,'course':c})

def editdetails(request,id):
    if request.method == 'POST':
        stu=Student.objects.get(id=id)
        stu.studentname=request.POST.get('sname')
        stu.address=request.POST.get('saddress')
        stu.age=request.POST.get('sage')
        stu.date=request.POST.get('date')
        sel=request.POST.get('sel')
        if sel:
            course=Course.objects.get(id=sel)
            stu.course=course
        stu.save()
        return redirect('studentdetails')
    return render(request,'editpage.html')


def delete(request,id):
    s=Student.objects.get(id=id)
    s.delete()
    return redirect('studentdetails')

