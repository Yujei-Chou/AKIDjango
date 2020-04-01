import json
from django.http import HttpResponseRedirect
from django.shortcuts import render
from alert import models
from django.core.paginator import Paginator
from django.db.models import Q
import pandas as pd
from django.contrib.auth.decorators import login_required


from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib import auth



def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/patient/')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/patient/')
    else:
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return render(request, "logout.html")

@login_required
def patient(request):

    articles = models.Patient.objects.all().order_by('uniquepid')
    paginator = Paginator(articles, 30)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    state = 'AKIPatients'
    context = {
        'contacts': contacts,
        'state': state,
    }
    return render(request, "patient.html", context)

@login_required
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

@login_required
def featureresult(request):
    articles = models.Allpt.objects.all()
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "featureresult.html", context)

@login_required
def queryfeatureresult(request,num):
    articles = models.Allpt.objects.filter(patientunitstayid=num)
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "featureresult.html", context)

@login_required
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

@login_required
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

@login_required
def diagnosis(request,num):
    articles = models.Diagnosis.objects.filter(patientunitstayid=num).order_by("diagnosisoffset")
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "diagnosis.html", context) #必须用这个return

@login_required
def infusiondrug(request,num):
    articles = models.Infusiondrug.objects.filter(patientunitstayid=num).filter(drugname__contains="NS").order_by("infusionoffset")
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "infusiondrug.html", context) #必须用这个return

@login_required
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

@login_required
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

@login_required
def medication(request,num):
    articles = models.Medication.objects.filter(patientunitstayid=num)
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "medication.html", context) #必须用这个return


@login_required
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

@login_required
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

@login_required
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

@login_required
def respiratorycharting(request,num):
    articles = models.Respiratorycharting.objects.filter(patientunitstayid=num).filter(respchartvaluelabel__contains="Tidal Volume").order_by("respchartoffset")
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "respiratorycharting.html", context) #必须用这个return

@login_required
def treatment(request,num):
    articles = models.Treatment.objects.filter(patientunitstayid=num).order_by("treatmentoffset")
    paginator = Paginator(articles, 30)  # Show 25 contacts per page
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts': contacts}

    return render(request, "treatment.html", context) #必须用这个return

@login_required
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

@login_required
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


@login_required
def PatientInHospital(request,num):
    articles = models.Patient.objects.filter(patienthealthsystemstayid=num)
    paginator = Paginator(articles, 30)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts':contacts}
    return render(request, "PatientInHospital.html", context)

@login_required
def PatientInUnit(request,num):
    articles = models.Patient.objects.filter(patientunitstayid=num)
    paginator = Paginator(articles, 30)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    context = {'contacts':contacts}
    return render(request, "PatientInUnit.html", context)

