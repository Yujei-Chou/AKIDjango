# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
# from django.db.models import Q
# from model_utils import Choices

class Hospital(models.Model):
    hospitalid = models.IntegerField(primary_key=True)
    numbedscategory = models.CharField(max_length=32, blank=True, null=True)
    teachingstatus = models.BooleanField(blank=True, null=True)
    region = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hospital'


class Patient(models.Model):
    patientunitstayid = models.IntegerField(primary_key=True)
    patienthealthsystemstayid = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=25, blank=True, null=True)
    age = models.CharField(max_length=10, blank=True, null=True)
    ethnicity = models.CharField(max_length=50, blank=True, null=True)
    hospitalid = models.ForeignKey(Hospital, models.DO_NOTHING, db_column='hospitalid', blank=True, null=True)
    wardid = models.IntegerField(blank=True, null=True)
    apacheadmissiondx = models.CharField(max_length=1000, blank=True, null=True)
    admissionheight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    hospitaladmittime24 = models.CharField(max_length=8, blank=True, null=True)
    hospitaladmitoffset = models.IntegerField(blank=True, null=True)
    hospitaladmitsource = models.CharField(max_length=30, blank=True, null=True)
    hospitaldischargeyear = models.SmallIntegerField(blank=True, null=True)
    hospitaldischargetime24 = models.CharField(max_length=8, blank=True, null=True)
    hospitaldischargeoffset = models.IntegerField(blank=True, null=True)
    hospitaldischargelocation = models.CharField(max_length=100, blank=True, null=True)
    hospitaldischargestatus = models.CharField(max_length=10, blank=True, null=True)
    unittype = models.CharField(max_length=50, blank=True, null=True)
    unitadmittime24 = models.CharField(max_length=8, blank=True, null=True)
    unitadmitsource = models.CharField(max_length=100, blank=True, null=True)
    unitvisitnumber = models.IntegerField(blank=True, null=True)
    unitstaytype = models.CharField(max_length=15, blank=True, null=True)
    admissionweight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    dischargeweight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    unitdischargetime24 = models.CharField(max_length=8, blank=True, null=True)
    unitdischargeoffset = models.IntegerField(blank=True, null=True)
    unitdischargelocation = models.CharField(max_length=100, blank=True, null=True)
    unitdischargestatus = models.CharField(max_length=10, blank=True, null=True)
    uniquepid = models.CharField(max_length=10, blank=True, null=True)
    numberoftimeinicu = models.CharField(max_length=10, blank=True, null=True)



    class Meta:
        managed = False
        db_table = 'patient'

class Admissiondrug(models.Model):
    admissiondrugid = models.IntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patientunitstayid')
    drugoffset = models.IntegerField()
    drugenteredoffset = models.IntegerField()
    drugnotetype = models.CharField(max_length=255, blank=True, null=True)
    specialtytype = models.CharField(max_length=255, blank=True, null=True)
    usertype = models.CharField(max_length=255)
    rxincluded = models.CharField(max_length=5, blank=True, null=True)
    writtenineicu = models.CharField(max_length=5, blank=True, null=True)
    drugname = models.CharField(max_length=255)
    drugdosage = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    drugunit = models.CharField(max_length=1000, blank=True, null=True)
    drugadmitfrequency = models.CharField(max_length=1000)
    drughiclseqno = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admissiondrug'


class Admissiondx(models.Model):
    admissiondxid = models.IntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patientunitstayid')
    admitdxenteredoffset = models.IntegerField()
    admitdxpath = models.CharField(max_length=500)
    admitdxname = models.CharField(max_length=255, blank=True, null=True)
    admitdxtext = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admissiondx'


class Allergy(models.Model):
    allergyid = models.IntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patientunitstayid')
    allergyoffset = models.IntegerField()
    allergyenteredoffset = models.IntegerField()
    allergynotetype = models.CharField(max_length=255, blank=True, null=True)
    specialtytype = models.CharField(max_length=255, blank=True, null=True)
    usertype = models.CharField(max_length=255)
    rxincluded = models.CharField(max_length=5, blank=True, null=True)
    writtenineicu = models.CharField(max_length=5, blank=True, null=True)
    drugname = models.CharField(max_length=255)
    allergytype = models.CharField(max_length=255, blank=True, null=True)
    allergyname = models.CharField(max_length=255, blank=True, null=True)
    drughiclseqno = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'allergy'


class Apacheapsvar(models.Model):
    apacheapsvarid = models.IntegerField(primary_key=True)
    #patientunitstayid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patientunitstayid', blank=True, null=True)
    patientunitstayid = models.OneToOneField(
        Patient,
        on_delete=models.CASCADE,
        related_name='connectID',
        db_column='patientunitstayid'
    )
    intubated = models.SmallIntegerField(blank=True, null=True)
    vent = models.SmallIntegerField(blank=True, null=True)
    dialysis = models.SmallIntegerField(blank=True, null=True)
    eyes = models.SmallIntegerField(blank=True, null=True)
    motor = models.SmallIntegerField(blank=True, null=True)
    verbal = models.SmallIntegerField(blank=True, null=True)
    meds = models.SmallIntegerField(blank=True, null=True)
    urine = models.FloatField(blank=True, null=True)
    wbc = models.FloatField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    respiratoryrate = models.FloatField(blank=True, null=True)
    sodium = models.FloatField(blank=True, null=True)
    heartrate = models.FloatField(blank=True, null=True)
    meanbp = models.FloatField(blank=True, null=True)
    ph = models.FloatField(blank=True, null=True)
    hematocrit = models.FloatField(blank=True, null=True)
    creatinine = models.FloatField(blank=True, null=True)
    albumin = models.FloatField(blank=True, null=True)
    pao2 = models.FloatField(blank=True, null=True)
    pco2 = models.FloatField(blank=True, null=True)
    bun = models.FloatField(blank=True, null=True)
    glucose = models.FloatField(blank=True, null=True)
    bilirubin = models.FloatField(blank=True, null=True)
    fio2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apacheapsvar'


class Apachepatientresult(models.Model):
    apachepatientresultsid = models.IntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patientunitstayid')
    physicianspeciality = models.CharField(max_length=50, blank=True, null=True)
    physicianinterventioncategory = models.CharField(max_length=50, blank=True, null=True)
    acutephysiologyscore = models.IntegerField(blank=True, null=True)
    apachescore = models.IntegerField(blank=True, null=True)
    apacheversion = models.CharField(max_length=5)
    predictedicumortality = models.CharField(max_length=50, blank=True, null=True)
    actualicumortality = models.CharField(max_length=50, blank=True, null=True)
    predictediculos = models.FloatField(blank=True, null=True)
    actualiculos = models.FloatField(blank=True, null=True)
    predictedhospitalmortality = models.CharField(max_length=50, blank=True, null=True)
    actualhospitalmortality = models.CharField(max_length=50, blank=True, null=True)
    predictedhospitallos = models.FloatField(blank=True, null=True)
    actualhospitallos = models.FloatField(blank=True, null=True)
    preopmi = models.IntegerField(blank=True, null=True)
    preopcardiaccath = models.IntegerField(blank=True, null=True)
    ptcawithin24h = models.IntegerField(blank=True, null=True)
    unabridgedunitlos = models.FloatField(blank=True, null=True)
    unabridgedhosplos = models.FloatField(blank=True, null=True)
    actualventdays = models.FloatField(blank=True, null=True)
    predventdays = models.FloatField(blank=True, null=True)
    unabridgedactualventdays = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apachepatientresult'


class Apachepredvar(models.Model):
    apachepredvarid = models.IntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patientunitstayid', blank=True, null=True)
    sicuday = models.SmallIntegerField(blank=True, null=True)
    saps3day1 = models.SmallIntegerField(blank=True, null=True)
    saps3today = models.SmallIntegerField(blank=True, null=True)
    saps3yesterday = models.SmallIntegerField(blank=True, null=True)
    gender = models.SmallIntegerField(blank=True, null=True)
    teachtype = models.SmallIntegerField(blank=True, null=True)
    region = models.SmallIntegerField(blank=True, null=True)
    bedcount = models.SmallIntegerField(blank=True, null=True)
    admitsource = models.SmallIntegerField(blank=True, null=True)
    graftcount = models.SmallIntegerField(blank=True, null=True)
    meds = models.SmallIntegerField(blank=True, null=True)
    verbal = models.SmallIntegerField(blank=True, null=True)
    motor = models.SmallIntegerField(blank=True, null=True)
    eyes = models.SmallIntegerField(blank=True, null=True)
    age = models.SmallIntegerField(blank=True, null=True)
    admitdiagnosis = models.CharField(max_length=11, blank=True, null=True)
    thrombolytics = models.SmallIntegerField(blank=True, null=True)
    diedinhospital = models.SmallIntegerField(blank=True, null=True)
    aids = models.SmallIntegerField(blank=True, null=True)
    hepaticfailure = models.SmallIntegerField(blank=True, null=True)
    lymphoma = models.SmallIntegerField(blank=True, null=True)
    metastaticcancer = models.SmallIntegerField(blank=True, null=True)
    leukemia = models.SmallIntegerField(blank=True, null=True)
    immunosuppression = models.SmallIntegerField(blank=True, null=True)
    cirrhosis = models.SmallIntegerField(blank=True, null=True)
    electivesurgery = models.SmallIntegerField(blank=True, null=True)
    activetx = models.SmallIntegerField(blank=True, null=True)
    readmit = models.SmallIntegerField(blank=True, null=True)
    ima = models.SmallIntegerField(blank=True, null=True)
    midur = models.SmallIntegerField(blank=True, null=True)
    ventday1 = models.SmallIntegerField(blank=True, null=True)
    oobventday1 = models.SmallIntegerField(blank=True, null=True)
    oobintubday1 = models.SmallIntegerField(blank=True, null=True)
    diabetes = models.SmallIntegerField(blank=True, null=True)
    managementsystem = models.SmallIntegerField(blank=True, null=True)
    var03hspxlos = models.FloatField(blank=True, null=True)
    pao2 = models.FloatField(blank=True, null=True)
    fio2 = models.FloatField(blank=True, null=True)
    ejectfx = models.FloatField(blank=True, null=True)
    creatinine = models.FloatField(blank=True, null=True)
    dischargelocation = models.SmallIntegerField(blank=True, null=True)
    visitnumber = models.SmallIntegerField(blank=True, null=True)
    amilocation = models.SmallIntegerField(blank=True, null=True)
    day1meds = models.SmallIntegerField(blank=True, null=True)
    day1verbal = models.SmallIntegerField(blank=True, null=True)
    day1motor = models.SmallIntegerField(blank=True, null=True)
    day1eyes = models.SmallIntegerField(blank=True, null=True)
    day1pao2 = models.FloatField(blank=True, null=True)
    day1fio2 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apachepredvar'


class Careplancareprovider(models.Model):
    cplcareprovderid = models.IntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patientunitstayid')
    careprovidersaveoffset = models.IntegerField()
    providertype = models.CharField(max_length=255, blank=True, null=True)
    specialty = models.CharField(max_length=255, blank=True, null=True)
    interventioncategory = models.CharField(max_length=255, blank=True, null=True)
    managingphysician = models.CharField(max_length=50, blank=True, null=True)
    activeupondischarge = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'careplancareprovider'


class Careplaneol(models.Model):
    cpleolid = models.IntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patientunitstayid')
    cpleolsaveoffset = models.IntegerField()
    cpleoldiscussionoffset = models.IntegerField(blank=True, null=True)
    activeupondischarge = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'careplaneol'


class Careplangeneral(models.Model):
    cplgeneralid = models.IntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patientunitstayid')
    activeupondischarge = models.CharField(max_length=10)
    cplitemoffset = models.IntegerField()
    cplgroup = models.CharField(max_length=255)
    cplitemvalue = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'careplangeneral'


class Careplangoal(models.Model):
    cplgoalid = models.IntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patientunitstayid')
    cplgoaloffset = models.IntegerField()
    cplgoalcategory = models.CharField(max_length=255, blank=True, null=True)
    cplgoalvalue = models.CharField(max_length=1000, blank=True, null=True)
    cplgoalstatus = models.CharField(max_length=255, blank=True, null=True)
    activeupondischarge = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'careplangoal'


class Careplaninfectiousdisease(models.Model):
    cplinfectid = models.IntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patientunitstayid')
    activeupondischarge = models.CharField(max_length=10)
    cplinfectdiseaseoffset = models.IntegerField()
    infectdiseasesite = models.CharField(max_length=64, blank=True, null=True)
    infectdiseaseassessment = models.CharField(max_length=64, blank=True, null=True)
    responsetotherapy = models.CharField(max_length=32, blank=True, null=True)
    treatment = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'careplaninfectiousdisease'


class Customlab(models.Model):
    customlabid = models.IntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patientunitstayid')
    labotheroffset = models.IntegerField()
    labothertypeid = models.IntegerField()
    labothername = models.CharField(max_length=64, blank=True, null=True)
    labotherresult = models.CharField(max_length=64, blank=True, null=True)
    labothervaluetext = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customlab'


class Diagnosis(models.Model):
    diagnosisid = models.IntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patientunitstayid')
    activeupondischarge = models.CharField(max_length=64, blank=True, null=True)
    diagnosisoffset = models.IntegerField()
    diagnosisstring = models.CharField(max_length=200)
    icd9code = models.CharField(max_length=100, blank=True, null=True)
    diagnosispriority = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'diagnosis'



class Infusiondrug(models.Model):
    infusiondrugid = models.IntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patientunitstayid')
    infusionoffset = models.IntegerField()
    drugname = models.CharField(max_length=255)
    drugrate = models.CharField(max_length=255, blank=True, null=True)
    infusionrate = models.CharField(max_length=255, blank=True, null=True)
    drugamount = models.CharField(max_length=255, blank=True, null=True)
    volumeoffluid = models.CharField(max_length=255, blank=True, null=True)
    patientweight = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'infusiondrug'


class Intakeoutput(models.Model):
    intakeoutputid = models.IntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patientunitstayid')
    intakeoutputoffset = models.IntegerField()
    intaketotal = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    outputtotal = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    dialysistotal = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    nettotal = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    intakeoutputentryoffset = models.IntegerField()
    cellpath = models.CharField(max_length=500, blank=True, null=True)
    celllabel = models.CharField(max_length=255, blank=True, null=True)
    cellvaluenumeric = models.DecimalField(max_digits=12, decimal_places=4)
    cellvaluetext = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'intakeoutput'


class Lab(models.Model):
    labid = models.IntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patientunitstayid')
    labresultoffset = models.IntegerField()
    labtypeid = models.DecimalField(max_digits=3, decimal_places=0)
    labname = models.CharField(max_length=256, blank=True, null=True)
    labresult = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    labresulttext = models.CharField(max_length=255, blank=True, null=True)
    labmeasurenamesystem = models.CharField(max_length=255, blank=True, null=True)
    labmeasurenameinterface = models.CharField(max_length=255, blank=True, null=True)
    labresultrevisedoffset = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab'


class Medication(models.Model):
    medicationid = models.IntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patientunitstayid')
    drugorderoffset = models.IntegerField()
    drugstartoffset = models.IntegerField()
    drugivadmixture = models.CharField(max_length=6)
    drugordercancelled = models.CharField(max_length=6)
    drugname = models.CharField(max_length=220, blank=True, null=True)
    drughiclseqno = models.IntegerField(blank=True, null=True)
    dosage = models.CharField(max_length=60, blank=True, null=True)
    routeadmin = models.CharField(max_length=120, blank=True, null=True)
    frequency = models.CharField(max_length=255, blank=True, null=True)
    loadingdose = models.CharField(max_length=120)
    prn = models.CharField(max_length=6)
    drugstopoffset = models.IntegerField()
    gtc = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'medication'


class Microlab(models.Model):
    microlabid = models.IntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patientunitstayid')
    culturetakenoffset = models.IntegerField()
    culturesite = models.CharField(max_length=255)
    organism = models.CharField(max_length=255)
    antibiotic = models.CharField(max_length=255, blank=True, null=True)
    sensitivitylevel = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'microlab'


class Note(models.Model):
    noteid = models.IntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patientunitstayid')
    noteoffset = models.IntegerField()
    noteenteredoffset = models.IntegerField()
    notetype = models.CharField(max_length=50)
    notepath = models.CharField(max_length=255)
    notevalue = models.CharField(max_length=150, blank=True, null=True)
    notetext = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'note'


class Nurseassessment(models.Model):
    nurseassessid = models.IntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patientunitstayid')
    nurseassessoffset = models.IntegerField()
    nurseassessentryoffset = models.IntegerField()
    cellattributepath = models.CharField(max_length=255)
    celllabel = models.CharField(max_length=255)
    cellattribute = models.CharField(max_length=255)
    cellattributevalue = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nurseassessment'


class Nursecare(models.Model):
    nursecareid = models.IntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patientunitstayid')
    celllabel = models.CharField(max_length=255)
    nursecareoffset = models.IntegerField()
    nursecareentryoffset = models.IntegerField()
    cellattributepath = models.CharField(max_length=255)
    cellattribute = models.CharField(max_length=255)
    cellattributevalue = models.CharField(max_length=4000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nursecare'


class Nursecharting(models.Model):
    nursingchartid = models.BigIntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patientunitstayid')
    nursingchartoffset = models.IntegerField()
    nursingchartentryoffset = models.IntegerField()
    nursingchartcelltypecat = models.CharField(max_length=255)
    nursingchartcelltypevallabel = models.CharField(max_length=255, blank=True, null=True)
    nursingchartcelltypevalname = models.CharField(max_length=255, blank=True, null=True)
    nursingchartvalue = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nursecharting'


class Pasthistory(models.Model):
    pasthistoryid = models.IntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='patientunitstayid')
    pasthistoryoffset = models.IntegerField()
    pasthistoryenteredoffset = models.IntegerField()
    pasthistorynotetype = models.CharField(max_length=40, blank=True, null=True)
    pasthistorypath = models.CharField(max_length=255)
    pasthistoryvalue = models.CharField(max_length=100, blank=True, null=True)
    pasthistoryvaluetext = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pasthistory'



class Physicalexam(models.Model):
    physicalexamid = models.IntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey(Patient, models.DO_NOTHING, db_column='patientunitstayid')
    physicalexamoffset = models.IntegerField()
    physicalexampath = models.CharField(max_length=255)
    physicalexamvalue = models.CharField(max_length=100, blank=True, null=True)
    physicalexamtext = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'physicalexam'


class Respiratorycare(models.Model):
    respcareid = models.IntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey(Patient, models.DO_NOTHING, db_column='patientunitstayid', blank=True, null=True)
    respcarestatusoffset = models.IntegerField(blank=True, null=True)
    currenthistoryseqnum = models.IntegerField(blank=True, null=True)
    airwaytype = models.CharField(max_length=30, blank=True, null=True)
    airwaysize = models.CharField(max_length=10, blank=True, null=True)
    airwayposition = models.CharField(max_length=32, blank=True, null=True)
    cuffpressure = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    ventstartoffset = models.IntegerField(blank=True, null=True)
    ventendoffset = models.IntegerField(blank=True, null=True)
    priorventstartoffset = models.IntegerField(blank=True, null=True)
    priorventendoffset = models.IntegerField(blank=True, null=True)
    apneaparams = models.CharField(max_length=80, blank=True, null=True)
    lowexhmvlimit = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    hiexhmvlimit = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    lowexhtvlimit = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    hipeakpreslimit = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    lowpeakpreslimit = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    hirespratelimit = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    lowrespratelimit = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    sighpreslimit = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    lowironoxlimit = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    highironoxlimit = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    meanairwaypreslimit = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    peeplimit = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    cpaplimit = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    setapneainterval = models.CharField(max_length=80, blank=True, null=True)
    setapneatv = models.CharField(max_length=80, blank=True, null=True)
    setapneaippeephigh = models.CharField(max_length=80, blank=True, null=True)
    setapnearr = models.CharField(max_length=80, blank=True, null=True)
    setapneapeakflow = models.CharField(max_length=80, blank=True, null=True)
    setapneainsptime = models.CharField(max_length=80, blank=True, null=True)
    setapneaie = models.CharField(max_length=80, blank=True, null=True)
    setapneafio2 = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'respiratorycare'


class Respiratorycharting(models.Model):
    respchartid = models.IntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey(Patient, models.DO_NOTHING, db_column='patientunitstayid', blank=True, null=True)
    respchartoffset = models.IntegerField(blank=True, null=True)
    respchartentryoffset = models.IntegerField(blank=True, null=True)
    respcharttypecat = models.CharField(max_length=255, blank=True, null=True)
    respchartvaluelabel = models.CharField(max_length=255, blank=True, null=True)
    respchartvalue = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'respiratorycharting'


class Treatment(models.Model):
    treatmentid = models.IntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey(Patient, models.DO_NOTHING, db_column='patientunitstayid', blank=True, null=True)
    treatmentoffset = models.IntegerField(blank=True, null=True)
    treatmentstring = models.CharField(max_length=200, blank=True, null=True)
    activeupondischarge = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'treatment'


class Vitalaperiodic(models.Model):
    vitalaperiodicid = models.IntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey(Patient, models.DO_NOTHING, db_column='patientunitstayid')
    observationoffset = models.IntegerField()
    noninvasivesystolic = models.FloatField(blank=True, null=True)
    noninvasivediastolic = models.FloatField(blank=True, null=True)
    noninvasivemean = models.FloatField(blank=True, null=True)
    paop = models.FloatField(blank=True, null=True)
    cardiacoutput = models.FloatField(blank=True, null=True)
    cardiacinput = models.FloatField(blank=True, null=True)
    svr = models.FloatField(blank=True, null=True)
    svri = models.FloatField(blank=True, null=True)
    pvr = models.FloatField(blank=True, null=True)
    pvri = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vitalaperiodic'


class Vitalperiodic(models.Model):
    vitalperiodicid = models.BigIntegerField(primary_key=True)
    patientunitstayid = models.ForeignKey(Patient, models.DO_NOTHING, db_column='patientunitstayid', blank=True, null=True)
    observationoffset = models.IntegerField(blank=True, null=True)
    temperature = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    sao2 = models.IntegerField(blank=True, null=True)
    heartrate = models.IntegerField(blank=True, null=True)
    respiration = models.IntegerField(blank=True, null=True)
    cvp = models.IntegerField(blank=True, null=True)
    etco2 = models.IntegerField(blank=True, null=True)
    systemicsystolic = models.IntegerField(blank=True, null=True)
    systemicdiastolic = models.IntegerField(blank=True, null=True)
    systemicmean = models.IntegerField(blank=True, null=True)
    pasystolic = models.IntegerField(blank=True, null=True)
    padiastolic = models.IntegerField(blank=True, null=True)
    pamean = models.IntegerField(blank=True, null=True)
    st1 = models.FloatField(blank=True, null=True)
    st2 = models.FloatField(blank=True, null=True)
    st3 = models.FloatField(blank=True, null=True)
    icp = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vitalperiodic'

class Allpt(models.Model):
    patientunitstayid = models.BigIntegerField(primary_key=True)
    age = models.FloatField(blank=True, null=True)
    nettotal = models.FloatField(blank=True, null=True)
    potassium_0 = models.FloatField(db_column='potassium 0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    potassium_1 = models.FloatField(db_column='potassium 1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    sodium_0 = models.FloatField(db_column='sodium 0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    sodium_1 = models.FloatField(db_column='sodium 1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    hct_0 = models.FloatField(db_column='Hct 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hct_1 = models.FloatField(db_column='Hct 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bun_0 = models.FloatField(db_column='BUN 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    bun_1 = models.FloatField(db_column='BUN 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ph_0 = models.FloatField(db_column='pH 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ph_1 = models.FloatField(db_column='pH 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    oi_0 = models.FloatField(db_column='OI 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    oi_1 = models.FloatField(db_column='OI 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tp_0 = models.FloatField(db_column='TP 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tp_1 = models.FloatField(db_column='TP 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tp_2 = models.FloatField(db_column='TP 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tp_3 = models.FloatField(db_column='TP 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tp_4 = models.FloatField(db_column='TP 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tp_5 = models.FloatField(db_column='TP 5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    urine_0 = models.FloatField(db_column='urine 0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    urine_1 = models.FloatField(db_column='urine 1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    urine_2 = models.FloatField(db_column='urine 2', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    urine_3 = models.FloatField(db_column='urine 3', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    urine_4 = models.FloatField(db_column='urine 4', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    urine_5 = models.FloatField(db_column='urine 5', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    diastolicbp_0 = models.FloatField(db_column='diastolicBP 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diastolicbp_1 = models.FloatField(db_column='diastolicBP 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diastolicbp_2 = models.FloatField(db_column='diastolicBP 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diastolicbp_3 = models.FloatField(db_column='diastolicBP 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diastolicbp_4 = models.FloatField(db_column='diastolicBP 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diastolicbp_5 = models.FloatField(db_column='diastolicBP 5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diastolicbp_6 = models.FloatField(db_column='diastolicBP 6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diastolicbp_7 = models.FloatField(db_column='diastolicBP 7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diastolicbp_8 = models.FloatField(db_column='diastolicBP 8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diastolicbp_9 = models.FloatField(db_column='diastolicBP 9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    diastolicbp10 = models.FloatField(db_column='diastolicBP10', blank=True, null=True)  # Field name made lowercase.
    diastolicbp11 = models.FloatField(db_column='diastolicBP11', blank=True, null=True)  # Field name made lowercase.
    diastolicbp12 = models.FloatField(db_column='diastolicBP12', blank=True, null=True)  # Field name made lowercase.
    diastolicbp13 = models.FloatField(db_column='diastolicBP13', blank=True, null=True)  # Field name made lowercase.
    diastolicbp14 = models.FloatField(db_column='diastolicBP14', blank=True, null=True)  # Field name made lowercase.
    diastolicbp15 = models.FloatField(db_column='diastolicBP15', blank=True, null=True)  # Field name made lowercase.
    diastolicbp16 = models.FloatField(db_column='diastolicBP16', blank=True, null=True)  # Field name made lowercase.
    diastolicbp17 = models.FloatField(db_column='diastolicBP17', blank=True, null=True)  # Field name made lowercase.
    diastolicbp18 = models.FloatField(db_column='diastolicBP18', blank=True, null=True)  # Field name made lowercase.
    diastolicbp19 = models.FloatField(db_column='diastolicBP19', blank=True, null=True)  # Field name made lowercase.
    systolicbp_0 = models.FloatField(db_column='systolicBP 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    systolicbp_1 = models.FloatField(db_column='systolicBP 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    systolicbp_2 = models.FloatField(db_column='systolicBP 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    systolicbp_3 = models.FloatField(db_column='systolicBP 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    systolicbp_4 = models.FloatField(db_column='systolicBP 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    systolicbp_5 = models.FloatField(db_column='systolicBP 5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    systolicbp_6 = models.FloatField(db_column='systolicBP 6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    systolicbp_7 = models.FloatField(db_column='systolicBP 7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    systolicbp_8 = models.FloatField(db_column='systolicBP 8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    systolicbp_9 = models.FloatField(db_column='systolicBP 9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    systolicbp10 = models.FloatField(db_column='systolicBP10', blank=True, null=True)  # Field name made lowercase.
    systolicbp11 = models.FloatField(db_column='systolicBP11', blank=True, null=True)  # Field name made lowercase.
    systolicbp12 = models.FloatField(db_column='systolicBP12', blank=True, null=True)  # Field name made lowercase.
    systolicbp13 = models.FloatField(db_column='systolicBP13', blank=True, null=True)  # Field name made lowercase.
    systolicbp14 = models.FloatField(db_column='systolicBP14', blank=True, null=True)  # Field name made lowercase.
    systolicbp15 = models.FloatField(db_column='systolicBP15', blank=True, null=True)  # Field name made lowercase.
    systolicbp16 = models.FloatField(db_column='systolicBP16', blank=True, null=True)  # Field name made lowercase.
    systolicbp17 = models.FloatField(db_column='systolicBP17', blank=True, null=True)  # Field name made lowercase.
    systolicbp18 = models.FloatField(db_column='systolicBP18', blank=True, null=True)  # Field name made lowercase.
    systolicbp19 = models.FloatField(db_column='systolicBP19', blank=True, null=True)  # Field name made lowercase.
    pulsep_0 = models.FloatField(db_column='pulseP 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pulsep_1 = models.FloatField(db_column='pulseP 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pulsep_2 = models.FloatField(db_column='pulseP 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pulsep_3 = models.FloatField(db_column='pulseP 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pulsep_4 = models.FloatField(db_column='pulseP 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pulsep_5 = models.FloatField(db_column='pulseP 5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pulsep_6 = models.FloatField(db_column='pulseP 6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pulsep_7 = models.FloatField(db_column='pulseP 7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pulsep_8 = models.FloatField(db_column='pulseP 8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pulsep_9 = models.FloatField(db_column='pulseP 9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pulsep10 = models.FloatField(db_column='pulseP10', blank=True, null=True)  # Field name made lowercase.
    pulsep11 = models.FloatField(db_column='pulseP11', blank=True, null=True)  # Field name made lowercase.
    pulsep12 = models.FloatField(db_column='pulseP12', blank=True, null=True)  # Field name made lowercase.
    pulsep13 = models.FloatField(db_column='pulseP13', blank=True, null=True)  # Field name made lowercase.
    pulsep14 = models.FloatField(db_column='pulseP14', blank=True, null=True)  # Field name made lowercase.
    pulsep15 = models.FloatField(db_column='pulseP15', blank=True, null=True)  # Field name made lowercase.
    pulsep16 = models.FloatField(db_column='pulseP16', blank=True, null=True)  # Field name made lowercase.
    pulsep17 = models.FloatField(db_column='pulseP17', blank=True, null=True)  # Field name made lowercase.
    pulsep18 = models.FloatField(db_column='pulseP18', blank=True, null=True)  # Field name made lowercase.
    pulsep19 = models.FloatField(db_column='pulseP19', blank=True, null=True)  # Field name made lowercase.
    shockid_0 = models.FloatField(db_column='shockID 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shockid_1 = models.FloatField(db_column='shockID 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shockid_2 = models.FloatField(db_column='shockID 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shockid_3 = models.FloatField(db_column='shockID 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shockid_4 = models.FloatField(db_column='shockID 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shockid_5 = models.FloatField(db_column='shockID 5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shockid_6 = models.FloatField(db_column='shockID 6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shockid_7 = models.FloatField(db_column='shockID 7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shockid_8 = models.FloatField(db_column='shockID 8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shockid_9 = models.FloatField(db_column='shockID 9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    shockid10 = models.FloatField(db_column='shockID10', blank=True, null=True)  # Field name made lowercase.
    shockid11 = models.FloatField(db_column='shockID11', blank=True, null=True)  # Field name made lowercase.
    meanbp_0 = models.FloatField(db_column='meanBP 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    meanbp_1 = models.FloatField(db_column='meanBP 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    meanbp_2 = models.FloatField(db_column='meanBP 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    meanbp_3 = models.FloatField(db_column='meanBP 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    meanbp_4 = models.FloatField(db_column='meanBP 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    meanbp_5 = models.FloatField(db_column='meanBP 5', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    meanbp_6 = models.FloatField(db_column='meanBP 6', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    meanbp_7 = models.FloatField(db_column='meanBP 7', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    meanbp_8 = models.FloatField(db_column='meanBP 8', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    meanbp_9 = models.FloatField(db_column='meanBP 9', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    meanbp10 = models.FloatField(db_column='meanBP10', blank=True, null=True)  # Field name made lowercase.
    meanbp11 = models.FloatField(db_column='meanBP11', blank=True, null=True)  # Field name made lowercase.
    meanbp12 = models.FloatField(db_column='meanBP12', blank=True, null=True)  # Field name made lowercase.
    meanbp13 = models.FloatField(db_column='meanBP13', blank=True, null=True)  # Field name made lowercase.
    meanbp14 = models.FloatField(db_column='meanBP14', blank=True, null=True)  # Field name made lowercase.
    meanbp15 = models.FloatField(db_column='meanBP15', blank=True, null=True)  # Field name made lowercase.
    meanbp16 = models.FloatField(db_column='meanBP16', blank=True, null=True)  # Field name made lowercase.
    meanbp17 = models.FloatField(db_column='meanBP17', blank=True, null=True)  # Field name made lowercase.
    meanbp18 = models.FloatField(db_column='meanBP18', blank=True, null=True)  # Field name made lowercase.
    meanbp19 = models.FloatField(db_column='meanBP19', blank=True, null=True)  # Field name made lowercase.
    tv_0 = models.FloatField(db_column='TV 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tv_1 = models.FloatField(db_column='TV 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tv_2 = models.FloatField(db_column='TV 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tv_3 = models.FloatField(db_column='TV 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ns_0 = models.FloatField(db_column='NS 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ns_1 = models.FloatField(db_column='NS 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ns_2 = models.FloatField(db_column='NS 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ns_3 = models.FloatField(db_column='NS 3', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ns_4 = models.FloatField(db_column='NS 4', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    weight_0 = models.FloatField(db_column='weight 0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    creatinine_0 = models.FloatField(db_column='creatinine 0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    creatinine_1 = models.FloatField(db_column='creatinine 1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    gfr_0 = models.FloatField(db_column='gfr 0', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    gfr_1 = models.FloatField(db_column='gfr 1', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    death = models.FloatField(db_column='Death', blank=True, null=True)  # Field name made lowercase.
    isdialysis = models.FloatField(db_column='IsDialysis', blank=True, null=True)  # Field name made lowercase.
    aki = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AllPT'
