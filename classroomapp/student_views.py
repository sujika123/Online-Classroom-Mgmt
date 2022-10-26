from django.contrib.auth import authenticate, login


# Create your views here.
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from classroomapp.forms import LoginForm, userloginform, courseddform, studentloginform, notificationform, \
    stdleavesheduleform, ComplaintForm, sAssignmentddform
from classroomapp.models import courseadd, studentadd, notificationadd, stdleaveshedule, teacherlogin, Complaint, \
    addnotes, taddAsgnmnttopic


def student(request):
    return render(request, 'student/dash.html')

def sprofileview(request):
    u = request.user
    data = studentadd.objects.filter(user=u)
    print(data)
    return render(request, 'student/profileview.html', {'data': data})

def sviewteachers(request):
    data=teacherlogin.objects.all()
    print(data)
    return render(request,'student/sviewteachers.html',{'data':data})

def sviewnotification(request):
    u = request.user
    data = notificationadd.objects.all()
    return render(request,'student/sviewnotification.html',{'data':data})

def sviewcourses(request):
    u = request.user
    data = courseadd.objects.all()
    return render(request,'student/viewcourses.html',{'data':data})

def sleaveshedule(request):
    form = stdleavesheduleform()
    if request.method == 'POST':
        form = stdleavesheduleform(request.POST)
        if form.is_valid():
            leave = form.save(commit=False)
            leave.name = request.user
            # leave.title=form.get('title')
            # leave.date=form.get('date')
            # leave.content=form.get('content')
            leave.save()
            return redirect('student')

    else:
        form = stdleavesheduleform()
    return render(request, 'student/sleaveshedule.html', {'form': form})


# def sleaveshedule(request):
#     form = stdleavesheduleform()
#     u = request.user
#     if request.method == 'POST':
#         form = stdleavesheduleform(request.POST, request.FILES)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.user = u
#             obj.save()
#         return redirect('sleavestatus')
#     return render(request, 'student/sleaveshedule.html', {'form': form})
#
#


def sleavestatus(request):
    u = request.user
    data = stdleaveshedule.objects.filter(name=u)
    print(data)

    return render(request, 'student/leavestatus.html', {'data': data})



def complaint_add_student(request):
    form = ComplaintForm()
    u = request.user
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request, 'Complaint Registered Successfully')
            return redirect('complaint_studentview')
    else:
        form = ComplaintForm()
    return render(request, 'student/complaintadd.html', {'form': form})



def complaint_studentview(request):
    n = Complaint.objects.filter(user=request.user)
    return render(request, 'student/viewcomplaint.html', {'complaint': n})


# Notes
def sviewnotes(request):
    u = request.user
    data = addnotes.objects.all()
    return render(request,'student/sviewnotes.html',{'data':data})


# Assignment
def sviewasgnmnttopic(request):
    u = request.user
    data = taddAsgnmnttopic.objects.all()
    return render(request,'student/sviewassignmenttopic.html',{'data':data})




def SaddAssignment(request):
    form = sAssignmentddform()
    u = request.user
    if request.method == 'POST':
        form = sAssignmentddform(request.POST,request.FILES)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.user=u
            obj.save()
        return redirect('student')
    return render(request,'student/saddassaignment.html',{'form':form})




