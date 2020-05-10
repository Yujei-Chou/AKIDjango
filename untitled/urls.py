"""meeting_hw3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from alert import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('logout/', views.logout),
    # path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('apacheapsvar/<str:num>/<str:feature>', views.apacheapsvar),
    path('customlab/<str:num>', views.customlab),
    path('diagnosis/<str:num>', views.diagnosis),
    path('infusiondrug/<str:num>', views.infusiondrug),
    path('intakeoutput/<str:num>/<str:feature>', views.intakeoutput),
    path('lab/<str:num>/<str:feature>', views.lab),
    path('nursecharting/<str:num>/<str:feature>', views.nursecharting),
    path('pasthistory/<str:num>/<str:feature>', views.pasthistory),
    path('physicalexam/<str:num>/<str:feature>', views.physicalexam),
    path('respiratorycharting/<str:num>', views.respiratorycharting),
    path('treatment/<str:num>', views.treatment),
    path('vitalaperiodic/<str:num>/<str:feature>', views.vitalaperiodic),
    path('vitalperiodic/<str:num>/<str:feature>', views.vitalperiodic),
    path('patient/', views.patient),
    path('predict/', views.predict),
    path('PredictResultForFile/', views.PredictResultForFile),
    path('PredictResultForInput/', views.PredictResultForInput),
    path('OnlyAKIPatient/', views.onlyAKIpatient),
    path('PatientInHospital/<str:num>', views.PatientInHospital),
    path('PatientInUnit/<str:num>', views.PatientInUnit),
    path('featureresult/',views.featureresult),
    path('featureresult/<str:num>',views.queryfeatureresult),


]
