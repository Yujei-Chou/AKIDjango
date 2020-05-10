import json
from django.http import HttpResponseRedirect
from django.shortcuts import render
from alert import models
from django.core.paginator import Paginator
from django.db.models import Q
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage


from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib import auth
import xgboost as xgb
import os
import numpy as np
import pickle
import glob



def ReplaceNan(l):
    for i,data in enumerate(l):
        if(data == ''):
            l[i] = '-10000'
    return l

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
def predict(request):
    ID = [0, 1, 2, 3, 4, 5]
    context = {
        'ID': ID,
    }

    return render(request, "predict.html", context)

@login_required
def PredictResultForInput(request):
    Crt=[]
    Intake=[]
    Urine=[]
    pH=[]
    Hct = []
    BUN=[]
    Na=[]
    K=[]
    TP=[]
    SystolicBP=[]
    MeanBP=[]
    MSI=[]
    eGFR=[]

    Age = []
    Weight = []
    Gender = ""
    temp=[]
    PredictRes = ""

    Agestr = ""
    Weightstr = ""
    Genderstr = ""

    filename = './AKIPatient/Xgboost_Seq.sav'
    Xgb_model = pickle.load(open(filename, 'rb'))
    if request.method == 'POST':
        if 'OnlyOneData' in request.POST:
            state = 'OnlyOneData'
            Age = request.POST['Age']
            Agestr = request.POST['Age']
            Weight = request.POST['Weight']
            Weightstr = request.POST['Weight']
            Gender = request.POST['Gender']
            Genderstr = request.POST['Gender']
            for i in range(0, 6):
                Crtstr = 'Crt_' + str(i)
                Intakestr = 'Intake_' + str(i)
                Urinestr = 'Urine_' + str(i)
                pHstr = 'pH_' + str(i)
                Hctstr = 'Hct_' + str(i)
                BUNstr = 'BUN_' + str(i)
                Nastr = 'Na_' + str(i)
                Kstr = 'K_' + str(i)
                TPstr = 'TP_' + str(i)
                SystolicBPstr = 'SystolicBP_' + str(i)
                MeanBPstr = 'MeanBP_' + str(i)
                MSIstr = 'MSI_' + str(i)
                eGFRstr = 'eGFR_' + str(i)

                Crt.append(request.POST[Crtstr])
                Intake.append(request.POST[Intakestr])
                Urine.append(request.POST[Urinestr])
                pH.append(request.POST[pHstr])
                Hct.append(request.POST[Hctstr])
                BUN.append(request.POST[BUNstr])
                Na.append(request.POST[Nastr])
                K.append(request.POST[Kstr])
                TP.append(request.POST[TPstr])
                SystolicBP.append(request.POST[SystolicBPstr])
                MeanBP.append(request.POST[MeanBPstr])
                MSI.append(request.POST[MSIstr])
                eGFR.append(request.POST[eGFRstr])

            Crt = list(map(float, ReplaceNan(Crt)))
            Intake = list(map(float, ReplaceNan(Intake)))
            Urine = list(map(float, ReplaceNan(Urine)))
            pH = list(map(float, ReplaceNan(pH)))
            Hct = list(map(float, ReplaceNan(Hct)))
            BUN = list(map(float, ReplaceNan(BUN)))
            Na = list(map(float, ReplaceNan(Na)))
            K = list(map(float, ReplaceNan(K)))
            TP = list(map(float, ReplaceNan(TP)))
            SystolicBP = list(map(float, ReplaceNan(SystolicBP)))
            MeanBP = list(map(float, ReplaceNan(MeanBP)))
            MSI = list(map(float, ReplaceNan(MSI)))
            eGFR = list(map(float, ReplaceNan(eGFR)))
            if(Gender == 'F'):
                Gender = '0'
            if(Gender == 'M'):
                Gender = '1'
            if(Gender == ''):
                Gender = '-10000'
            if(Weight == ''):
                Weight = '-10000'
            if(Age == ''):
                Age = '-10000'

            X = np.array([Crt, Intake, Urine, pH, Hct, BUN, Na, K, TP, SystolicBP, MeanBP, MSI, eGFR])
            X = X.reshape(1, -1)
            X = np.insert(X, 0, float(Gender), axis=1)
            X = np.insert(X, 0, float(Weight), axis=1)
            X = np.insert(X, 0, float(Age), axis=1)
            Y = Xgb_model.predict(X)

    context = {
        'PredictRes': PredictRes,
        'Crt': Crt, 'Intake': Intake, 'Urine': Urine, 'pH': pH, 'Hct': Hct, 'BUN': BUN,
        'Na': Na, 'K': K, 'TP': TP, 'SystolicBP': SystolicBP, 'MeanBP': MeanBP, 'MSI': MSI, 'eGFR': eGFR,
        'Agestr': Agestr, 'Weightstr': Weightstr, 'Genderstr': Genderstr,
    }
    return render(request, "PredictResultForInput.html", context)

@login_required
def PredictResultForFile(request):
    filename = './AKIPatient/Xgboost_Seq.sav'
    Xgb_model = pickle.load(open(filename, 'rb'))
    if request.method == 'POST':
        if 'Upload' in request.POST:
            state = 'Upload'
            UploadFile = request.FILES['document']
            fs = FileSystemStorage()
            fs.save('File', UploadFile)
            for filename in os.listdir("./media"):
                if(filename != "File"):
                    file = "./media/" + filename
                    os.remove(file)
    File_df = pd.read_csv('./media/File', sep=',', header=0, encoding='utf-8')
    test = File_df.fillna(-10000)
    X = test.to_numpy()
    Y = Xgb_model.predict(X)
    File_df['AKI'] = Y
    res = []
    for i in range(0, len(File_df)):
        DictTemp = {
            'age': File_df['age'][i],
            'weight': File_df['weight'][i],
            'gender': File_df['gender'].map({1: "M", 0: "F"})[i],
            'crt': File_df.loc[i, ['creatinine_seq_0', 'creatinine_seq_1', 'creatinine_seq_2', 'creatinine_seq_3', 'creatinine_seq_4', 'creatinine_seq_5']].tolist(),
            'intake': File_df.loc[i, ['intake_seq_0', 'intake_seq_1', 'intake_seq_2', 'intake_seq_3', 'intake_seq_4', 'intake_seq_5']].tolist(),
            'urine': File_df.loc[i, ['urine_seq_0', 'urine_seq_1', 'urine_seq_2', 'urine_seq_3', 'urine_seq_4', 'urine_seq_5']].tolist(),
            'pH': File_df.loc[i, ['pH_seq_0', 'pH_seq_1', 'pH_seq_2', 'pH_seq_3', 'pH_seq_4', 'pH_seq_5']].tolist(),
            'Hct': File_df.loc[i, ['Hct_seq_0', 'Hct_seq_1', 'Hct_seq_2', 'Hct_seq_3', 'Hct_seq_4', 'Hct_seq_5']].tolist(),
            'BUN': File_df.loc[i, ['BUN_seq_0', 'BUN_seq_1', 'BUN_seq_2', 'BUN_seq_3', 'BUN_seq_4', 'BUN_seq_5']].tolist(),
            'Na': File_df.loc[i, ['Na_seq_0', 'Na_seq_1', 'Na_seq_2', 'Na_seq_3', 'Na_seq_4', 'Na_seq_5']].tolist(),
            'K': File_df.loc[i, ['K_seq_0', 'K_seq_1', 'K_seq_2', 'K_seq_3', 'K_seq_4', 'K_seq_5']].tolist(),
            'TP': File_df.loc[i, ['TP_seq_0', 'TP_seq_1', 'TP_seq_2', 'TP_seq_3', 'TP_seq_4', 'TP_seq_5']].tolist(),
            'systolicBP': File_df.loc[i, ['systolicBP_seq_0', 'systolicBP_seq_1', 'systolicBP_seq_2', 'systolicBP_seq_3', 'systolicBP_seq_4', 'systolicBP_seq_5']].tolist(),
            'meanBP': File_df.loc[i, ['meanBP_seq_0', 'meanBP_seq_1', 'meanBP_seq_2', 'meanBP_seq_3', 'meanBP_seq_4', 'meanBP_seq_5']].tolist(),
            'MSI': File_df.loc[i, ['MSI_seq_0', 'MSI_seq_1', 'MSI_seq_2', 'MSI_seq_3', 'MSI_seq_4', 'MSI_seq_5']].tolist(),
            'eGFR': File_df.loc[i, ['eGFR_seq_0', 'eGFR_seq_1', 'eGFR_seq_2', 'eGFR_seq_3', 'eGFR_seq_4', 'eGFR_seq_5']].tolist(),
            'aki': File_df['AKI'][i],
        }
        res.append(DictTemp)

    paginator = Paginator(res, 1)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)

    context = {
        'contacts': contacts,
    }
    return render(request, "PredictResultForFile.html", context)


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

