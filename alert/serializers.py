from rest_framework import serializers
from alert.models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        # fields = '__all__'
        fields = ('id', 'patientunitstayid', 'gender', 'age')