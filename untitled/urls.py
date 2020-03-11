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
from alert.views import hello_view
from alert import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('hello/', hello_view),
    path('admissiondrug/<str:num>', views.admissiondrug),
    path('admissiondx/<str:num>', views.admissiondx),
    path('allergy/<str:num>', views.allergy),
    path('apacheapsvar/<str:num>/<str:feature>', views.apacheapsvar),
    path('apachepatientresult/<str:num>', views.apachepatientresult),
    path('apachepredvar/<str:num>', views.apachepredvar),
    path('careplancareprovider/<str:num>', views.careplancareprovider),
    path('careplaneol/<str:num>', views.careplaneol),
    path('careplangeneral/<str:num>', views.careplangeneral),
    path('careplangoal/<str:num>', views.careplangoal),
    path('careplaninfectiousdisease/<str:num>', views.careplaninfectiousdisease),
    path('customlab/<str:num>', views.customlab),
    path('diagnosis/<str:num>', views.diagnosis),
    path('hospital/<str:num>', views.hospital),
    path('infusiondrug/<str:num>', views.infusiondrug),
    path('intakeoutput/<str:num>/<str:feature>', views.intakeoutput),
    path('lab/<str:num>/<str:feature>', views.lab),
    path('medication/<str:num>', views.medication),
    path('microlab/<str:num>', views.microlab),
    path('note/<str:num>', views.note),
    path('nurseassessment/<str:num>', views.nurseassessment),
    path('nursecare/<str:num>', views.nursecare),
    path('nursecharting/<str:num>/<str:feature>', views.nursecharting),
    path('pasthistory/<str:num>/<str:feature>', views.pasthistory),
    path('physicalexam/<str:num>/<str:feature>', views.physicalexam),
    path('respiratorycare/<str:num>', views.respiratorycare),
    path('respiratorycharting/<str:num>', views.respiratorycharting),
    path('treatment/<str:num>', views.treatment),
    path('vitalaperiodic/<str:num>/<str:feature>', views.vitalaperiodic),
    path('vitalperiodic/<str:num>/<str:feature>', views.vitalperiodic),
    path('patient/', views.patient),
    path('OnlyAKIPatient/', views.onlyAKIpatient),
    path('PatientInHospital/<str:num>', views.PatientInHospital),
    path('PatientInUnit/<str:num>', views.PatientInUnit),
    path('featureresult/',views.featureresult),
    path('featureresult/<str:num>',views.queryfeatureresult),
    path('linkHospital/<str:num>',views.linkHospital),

]
