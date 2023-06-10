from django.shortcuts import render, get_object_or_404,redirect
from classroom.forms import StudentSignUpForm, LoginForm, TeacherSignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  (View,TemplateView,
                                  ListView,DetailView,
                                  CreateView,UpdateView,
                                  DeleteView)
from classroom import models
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def home(request):
    return render(request,'home.html', {})

def SignUp(request):
    return render(request,'classroom/signup.html',{})


def StudentSignup(request):
    msg = None
    if request.method == 'POST':
        form =StudentSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = StudentSignUpForm()
    return render(request,'studentsignup.html', {'form': form, 'msg': msg})

def TeacherSignup(request):
    msg = None
    if request.method == 'POST':
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = TeacherSignUpForm()
    return render(request,'teachersignup.html', {'form': form, 'msg': msg})


## User Profile of student.
def student_detail(request):
    return render(request,'student_detail.html')

## User Profile for teacher.
def teacher_detail(request):
    return render(request,'teacher_detail.html')



def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(f"{user.is_teacher}")
            if user is not None and user.is_student:
                login(request, user)
                return redirect('student_detail')
            elif user is not None and user.is_teacher:
                login(request, user)
                return redirect('teacher_detail')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


## logout view.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def SignUp(request):
    return render(request,'signup.html',{})