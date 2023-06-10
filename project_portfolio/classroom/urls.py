from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login_view, name='login_view'),
    path('signup', views.SignUp, name='SignUp'),
    path('studentsignup/', views.StudentSignup, name='StudentSignup'),
    path('teachersignup/', views.TeacherSignup, name='TeacherSignup'),
    path('logout/',views.user_logout,name="logout"),
    path('student_detail/',views.student_detail,name="student_detail"),
    path('teacher_detail/',views.teacher_detail,name="teacher_detail"),
    ]