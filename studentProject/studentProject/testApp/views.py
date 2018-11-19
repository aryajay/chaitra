from django.shortcuts import render
from testApp.models import Student

# Create your views here.
def home(request):
    return render(request,'testApp/home.html')

def studentInfo(request):
    student_list=Student.objects.all()
    my_dict={'student_list':student_list}
    return render(request,'testApp/studentinfo.html',context=my_dict)
