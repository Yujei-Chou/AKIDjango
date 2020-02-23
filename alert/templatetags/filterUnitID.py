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
    HospitalIDList = Patient.objects.filter(uniquepid=uniquepid)
    for data in HospitalIDList:
        if(data.hospitaldischargestatus == "Expired"):
            res = "Expired"
            break
    return res
