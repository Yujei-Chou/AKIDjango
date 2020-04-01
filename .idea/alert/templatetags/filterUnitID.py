from django import template
from alert.models import Patient
import numpy as np
register = template.Library()

@register.filter
def filterUnitID(patienthealthsystemstayid):
    ICUList = Patient.objects.filter(patienthealthsystemstayid=patienthealthsystemstayid)
    return ICUList

@register.filter
def filterHospitalID(uniquepid):
    HospitalIDList = Patient.objects.filter(uniquepid=uniquepid).order_by('patienthealthsystemstayid')
    return HospitalIDList


@register.filter
def DischargeHosStatus(uniquepid):
    res = "Alive"
    cnt = Patient.objects.filter(uniquepid=uniquepid).filter(hospitaldischargestatus="Expired")
    if(cnt.count() > 0):
        res = "Expired"
    # res = "Alive"
    # HospitalIDList = Patient.objects.filter(uniquepid=uniquepid)
    # for data in HospitalIDList:
    #     if(data.hospitaldischargestatus == "Expired"):
    #         res = "Expired"
    #         break
    return res

@register.filter
def timeInICU(value):
    if(value == 1 or value is None):
        res = "1st time in icu"
    elif(value == 2):
        res = "2nd time in icu"
    elif(value == 3):
        res = "3rd time in icu"
    else:
        res = str(value)+"th time in icu"
    return res