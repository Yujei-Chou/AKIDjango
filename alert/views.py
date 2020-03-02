import json
from django.http import HttpResponse
from django.shortcuts import render
from alert import models
from django.core.paginator import Paginator
from django.db.models import Q
import pandas as pd
import numpy as np
# # for rest_framework
# from alert.serializers import PatientSerializer
# from rest_framework import viewsets
# from rest_framework import viewsets, status
# from rest_framework.response import Response
#
# from django.template.response import TemplateResponse
# from django.http.response import HttpResponse
# from alert.models import query_alert_by_args
# # Create your views here.


# def patient(request):
#     html = TemplateResponse(request ,'patient.html')
#     return HttpResponse(html.render())
#
# class PatientViewSet(viewsets.ModelViewSet):
#     queryset = models.Patient.objects.all()
#     serializer_class = PatientSerializer
#
#     def list(self, request, **kwargs):
#         try:
#             music = query_alert_by_args(**request.query_params)
#             serializer = PatientSerializer(patient['items'], many=True)
#             result = dict()
#             result['data'] = serializer.data
#             result['draw'] = patient['draw']
#             result['recordsTotal'] = patient['total']
#             result['recordsFiltered'] = patient['count']
#             return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)
#
#         except Exception as e:
#             return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)


# def patient(req):
#     users_list = []
#     res = models.Patient.objects.all()
#     for item in res:
#         user_info = {
#             "patientunitstayid":item.patientunitstayid,
#             "age":item.age,
#             "gender":item.gender,
#         }
#         users_list.append(user_info)
#     user_dic = {}
#     print(users_list)
#     user_dic["data"] = users_list#按照官方文件的格式寫
#     return HttpResponse(json.dumps(user_dic))

def hello_view(request):
    return render(request, 'hello_django.html', {
        'data': "",
    })

def patient(request):
    SampleAllPatients_df = pd.read_csv("./AKIPatient/SampleAllPatients.csv", sep=',', header=0, encoding='utf-8')
    articles = models.Patient.objects.filter(patientunitstayid__in=SampleAllPatients_df['patientunitstayid']).order_by('uniquepid')
    paginator = Paginator(articles, 30)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    state = 'AKIPatients'
    context = {
        'contacts': contacts,
        'state': state,
    }
    return render(request, "patient.html", context)

def onlyAKIpatient(request):
    AKIPatients_df = pd.read_csv("./AKIPatient/AKIPatients.csv", sep=',', header=0, encoding='utf-8')
    articles = models.Patient.objects.filter(patientunitstayid__in=AKIPatients_df['patientunitstayid']).order_by('uniquepid')
    # articles = models.Patient.objects.all()
    paginator = Paginator(articles, 30)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    state = 'AllPatients'
    context = {
        'contacts': contacts,
        'state': state,
    }
    return render(request, "patient.html", context)
def filterUnitID(request, num):
    ICUList = models.Patient.objects.filter(uniquepid=num)
    return render(request, "patient.html", {'ICUList': ICUList})

def admissiondrug(request,num):
    #articles = models.Admissiondrug.objects.all()
    articles = models.Admissiondrug.objects.filter(patientunitstayid=num)
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "admissiondrug.html", context) #必须用这个return

def admissiondx(request,num):
    articles = models.Admissiondx.objects.filter(patientunitstayid=num)
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "admissiondx.html", context) #必须用这个return

def allergy(request,num):
    articles = models.Allergy.objects.filter(patientunitstayid=num)
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "allergy.html", context) #必须用这个return

def apacheapsvar(request,num,feature):
    articles = models.Apacheapsvar.objects.filter(patientunitstayid=num)
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {
        'contacts': contacts,
        'feature': feature,
    }

    return render(request, "apacheapsvar.html", context) #必须用这个return

def apachepatientresult(request,num):
    articles = models.Apachepatientresult.objects.filter(patientunitstayid=num)
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "apachepatientresult.html", context) #必须用这个return

def apachepredvar(request,num):
    articles = models.Apachepredvar.objects.filter(patientunitstayid=num)
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "apachepredvar.html", context) #必须用这个return

def careplancareprovider(request,num):
    articles = models.Careplancareprovider.objects.filter(patientunitstayid=num)
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "careplancareprovider.html", context) #必须用这个return
def careplaneol(request,num):
    articles = models.Careplaneol.objects.filter(patientunitstayid=num)
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "careplaneol.html", context) #必须用这个return
def careplangeneral(request,num):
    articles = models.Careplangeneral.objects.filter(patientunitstayid=num)
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "careplangeneral.html", context) #必须用这个return

def careplangoal(request,num):
    articles = models.Careplangoal.objects.filter(patientunitstayid=num)
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "careplangoal.html", context) #必须用这个return

def careplaninfectiousdisease(request,num):
    articles = models.Careplaninfectiousdisease.objects.filter(patientunitstayid=num)
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "careplaninfectiousdisease.html", context) #必须用这个return

def customlab(request,num):
    articles = models.Customlab.objects.filter(patientunitstayid=num).filter(labothername__icontains="est GFR").order_by("labotheroffset")
    # if(feature == "GFR"):
    #     articles = models.Customlab.objects.filter(patientunitstayid=num).filter(labothername__contains="GFR").order_by("labotheroffset")
    # else:
    #     articles = models.Customlab.objects.filter(patientunitstayid=num)
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "customlab.html", context) #必须用这个return

def diagnosis(request,num):
    articles = models.Diagnosis.objects.filter(patientunitstayid=num).order_by("diagnosisoffset")
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "diagnosis.html", context) #必须用这个return

def hospital(request,num):
    articles = models.Hospital.objects.filter(patientunitstayid=num)
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "hospital.html", context) #必须用这个return

def infusiondrug(request,num):
    articles = models.Infusiondrug.objects.filter(patientunitstayid=num).filter(drugname__contains="NS").order_by("infusionoffset")
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "infusiondrug.html", context) #必须用这个return

def intakeoutput(request,num,feature):
    if(feature == "urine"):
        articles = models.Intakeoutput.objects.filter(patientunitstayid=num).filter(celllabel__contains="Urine").order_by("intakeoutputoffset")
    elif(feature == "weight"):
        articles = models.Intakeoutput.objects.filter(patientunitstayid=num).filter(celllabel__contains="Bodyweight").order_by("intakeoutputoffset")
    elif(feature == "netfluid"):
        articles = models.Intakeoutput.objects.filter(patientunitstayid=num).order_by("intakeoutputoffset")
    elif(feature == "NS"):
        articles = models.Intakeoutput.objects.filter(patientunitstayid=num).filter(celllabel__contains="NS").order_by("intakeoutputoffset")
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "intakeoutput.html", context) #必须用这个return

def lab(request,num,feature):
    if(feature == "creatinine"):
        articles = models.Lab.objects.filter(patientunitstayid=num).filter(labname__contains="creatinine").order_by("labresultoffset")
    elif(feature == "BUN"):
        articles = models.Lab.objects.filter(patientunitstayid=num).filter(labname="BUN").order_by("labresultoffset")
    elif(feature == "PH"):
        articles = models.Lab.objects.filter(patientunitstayid=num).filter(labname="pH").order_by("labresultoffset")
    elif(feature == "Ca_K"):
        articles = models.Lab.objects.filter(patientunitstayid=num).filter(Q(labname="sodium")|Q(labname="potassium")).order_by("labresultoffset")
    elif(feature == "HCT"):
        articles = models.Lab.objects.filter(patientunitstayid=num).filter(labname="Hct").order_by("labresultoffset")
    elif (feature == "paO2_FiO2"):
        articles = models.Lab.objects.filter(patientunitstayid=num).filter(Q(labname="paO2") | Q(labname="FiO2")).order_by("labresultoffset")
    else:
        articles = models.Lab.objects.filter(patientunitstayid=num)

    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "lab.html", context) #必须用这个return

def medication(request,num):
    articles = models.Medication.objects.filter(patientunitstayid=num)
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "medication.html", context) #必须用这个return

def microlab(request,num):
    articles = models.Microlab.objects.filter(patientunitstayid=num)
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "microlab.html", context) #必须用这个return

def note(request,num):
    articles = models.Note.objects.filter(patientunitstayid=num)
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "note.html", context) #必须用这个return

def nurseassessment(request,num):
    articles = models.Nurseassessment.objects.filter(patientunitstayid=num)
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "nurseassessment.html", context) #必须用这个return

def nursecare(request,num):
    articles = models.Nursecare.objects.filter(patientunitstayid=num)
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "nursecare.html", context) #必须用这个return

def nursecharting(request,num,feature):
    if(feature == "temperature"):
        articles = models.Nursecharting.objects.filter(patientunitstayid=num).filter(nursingchartcelltypevallabel="Temperature").order_by('nursingchartoffset')
    elif(feature == "SystolicBP_Data"):
        articles = models.Nursecharting.objects.filter(patientunitstayid=num).filter(nursingchartcelltypevalname="Non-Invasive BP Systolic").order_by('nursingchartoffset')
    elif(feature == "DiastolicBP_Data"):
        articles = models.Nursecharting.objects.filter(patientunitstayid=num).filter(nursingchartcelltypevalname="Non-Invasive BP Diastolic").order_by('nursingchartoffset')
    else:
        articles = models.Nursecharting.objects.filter(patientunitstayid=num)
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "nursecharting.html", context) #必须用这个return

def pasthistory(request,num,feature):
    if(feature == "creatinine"):
        articles = models.Pasthistory.objects.filter(patientunitstayid=num).filter(pasthistoryvaluetext__contains="creatinine").order_by("pasthistoryoffset")
    else:
        articles = models.Pasthistory.objects.filter(patientunitstayid=num).order_by("pasthistoryoffset")
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "pasthistory.html", context) #必须用这个return

def physicalexam(request,num,feature):
    if(feature == "urine"):
        articles = models.Physicalexam.objects.filter(patientunitstayid=num).filter(physicalexamvalue__contains="Urine").order_by("physicalexamoffset")
    elif(feature == "Hemodynamic_Data"):
        articles = models.Physicalexam.objects.filter(patientunitstayid=num).filter(physicalexampath__contains="Hemodynamic Data").order_by("physicalexamoffset")
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "physicalexam.html", context) #必须用这个return

def respiratorycare(request,num):
    articles = models.Respiratorycare.objects.filter(patientunitstayid=num)
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "respiratorycare.html", context) #必须用这个return

def respiratorycharting(request,num):
    articles = models.Respiratorycharting.objects.filter(patientunitstayid=num).filter(respchartvaluelabel__contains="Tidal Volume").order_by("respchartoffset")
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "respiratorycharting.html", context) #必须用这个return

def treatment(request,num):
    articles = models.Treatment.objects.filter(patientunitstayid=num).order_by("treatmentoffset")
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "treatment.html", context) #必须用这个return

def vitalaperiodic(request,num,feature):
    if(feature == "SystolicBP_Data"):
        articles = models.Vitalaperiodic.objects.filter(patientunitstayid=num).exclude(noninvasivesystolic__isnull=True).order_by("observationoffset")
    elif(feature == "DiastolicBP_Data"):
        articles = models.Vitalaperiodic.objects.filter(patientunitstayid=num).exclude(noninvasivediastolic__isnull=True).order_by("observationoffset")
    elif(feature == "Hemodynamic_Data"):
        articles = models.Vitalaperiodic.objects.filter(patientunitstayid=num).exclude(svr__isnull=True).order_by("observationoffset")
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {
        'contacts': contacts,
        'feature': feature,
    }
    return render(request, "vitalaperiodic.html", context) #必须用这个return

def vitalperiodic(request,num,feature):
    if(feature == "temperature"):
        articles = models.Vitalperiodic.objects.filter(patientunitstayid=num).exclude(temperature__isnull=True).order_by("observationoffset")
    elif(feature == "Hemodynamic_Data"):
        articles = models.Vitalperiodic.objects.filter(patientunitstayid=num).exclude(cvp__isnull=True).order_by("observationoffset")
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {
        'contacts': contacts,
        'feature': feature,
    }

    return render(request, "vitalperiodic.html", context) #必须用这个return


def PatientInHospital(request,num):
    articles = models.Patient.objects.filter(patienthealthsystemstayid=num)
    paginator = Paginator(articles, 30)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts':contacts}
    return render(request, "PatientInHospital.html", context)

def PatientInUnit(request,num):
    articles = models.Patient.objects.filter(patientunitstayid=num)
    paginator = Paginator(articles, 30)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts':contacts}
    return render(request, "PatientInUnit.html", context)

def linkHospital(request,num):
    articles = models.Hospital.objects.filter(hospitalid=num)
    paginator = Paginator(articles, 30)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts':contacts}
    return render(request, "hospital.html", context)