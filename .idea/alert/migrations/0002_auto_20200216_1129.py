# Generated by Django 3.0 on 2020-02-16 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alert', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admissiondrug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admissiondrugid', models.IntegerField()),
                ('drugoffset', models.IntegerField()),
                ('drugenteredoffset', models.IntegerField()),
                ('drugnotetype', models.CharField(blank=True, max_length=255, null=True)),
                ('specialtytype', models.CharField(blank=True, max_length=255, null=True)),
                ('usertype', models.CharField(max_length=255)),
                ('rxincluded', models.CharField(blank=True, max_length=5, null=True)),
                ('writtenineicu', models.CharField(blank=True, max_length=5, null=True)),
                ('drugname', models.CharField(max_length=255)),
                ('drugdosage', models.DecimalField(blank=True, decimal_places=4, max_digits=11, null=True)),
                ('drugunit', models.CharField(blank=True, max_length=1000, null=True)),
                ('drugadmitfrequency', models.CharField(max_length=1000)),
                ('drughiclseqno', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'admissiondrug',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Admissiondx',
            fields=[
                ('admissiondxid', models.IntegerField(primary_key=True, serialize=False)),
                ('admitdxenteredoffset', models.IntegerField()),
                ('admitdxpath', models.CharField(max_length=500)),
                ('admitdxname', models.CharField(blank=True, max_length=255, null=True)),
                ('admitdxtext', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'admissiondx',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergyid', models.IntegerField()),
                ('allergyoffset', models.IntegerField()),
                ('allergyenteredoffset', models.IntegerField()),
                ('allergynotetype', models.CharField(blank=True, max_length=255, null=True)),
                ('specialtytype', models.CharField(blank=True, max_length=255, null=True)),
                ('usertype', models.CharField(max_length=255)),
                ('rxincluded', models.CharField(blank=True, max_length=5, null=True)),
                ('writtenineicu', models.CharField(blank=True, max_length=5, null=True)),
                ('drugname', models.CharField(max_length=255)),
                ('allergytype', models.CharField(blank=True, max_length=255, null=True)),
                ('allergyname', models.CharField(blank=True, max_length=255, null=True)),
                ('drughiclseqno', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'allergy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Apacheapsvar',
            fields=[
                ('apacheapsvarid', models.IntegerField(primary_key=True, serialize=False)),
                ('intubated', models.SmallIntegerField(blank=True, null=True)),
                ('vent', models.SmallIntegerField(blank=True, null=True)),
                ('dialysis', models.SmallIntegerField(blank=True, null=True)),
                ('eyes', models.SmallIntegerField(blank=True, null=True)),
                ('motor', models.SmallIntegerField(blank=True, null=True)),
                ('verbal', models.SmallIntegerField(blank=True, null=True)),
                ('meds', models.SmallIntegerField(blank=True, null=True)),
                ('urine', models.FloatField(blank=True, null=True)),
                ('wbc', models.FloatField(blank=True, null=True)),
                ('temperature', models.FloatField(blank=True, null=True)),
                ('respiratoryrate', models.FloatField(blank=True, null=True)),
                ('sodium', models.FloatField(blank=True, null=True)),
                ('heartrate', models.FloatField(blank=True, null=True)),
                ('meanbp', models.FloatField(blank=True, null=True)),
                ('ph', models.FloatField(blank=True, null=True)),
                ('hematocrit', models.FloatField(blank=True, null=True)),
                ('creatinine', models.FloatField(blank=True, null=True)),
                ('albumin', models.FloatField(blank=True, null=True)),
                ('pao2', models.FloatField(blank=True, null=True)),
                ('pco2', models.FloatField(blank=True, null=True)),
                ('bun', models.FloatField(blank=True, null=True)),
                ('glucose', models.FloatField(blank=True, null=True)),
                ('bilirubin', models.FloatField(blank=True, null=True)),
                ('fio2', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'apacheapsvar',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Apachepatientresult',
            fields=[
                ('apachepatientresultsid', models.IntegerField(primary_key=True, serialize=False)),
                ('physicianspeciality', models.CharField(blank=True, max_length=50, null=True)),
                ('physicianinterventioncategory', models.CharField(blank=True, max_length=50, null=True)),
                ('acutephysiologyscore', models.IntegerField(blank=True, null=True)),
                ('apachescore', models.IntegerField(blank=True, null=True)),
                ('apacheversion', models.CharField(max_length=5)),
                ('predictedicumortality', models.CharField(blank=True, max_length=50, null=True)),
                ('actualicumortality', models.CharField(blank=True, max_length=50, null=True)),
                ('predictediculos', models.FloatField(blank=True, null=True)),
                ('actualiculos', models.FloatField(blank=True, null=True)),
                ('predictedhospitalmortality', models.CharField(blank=True, max_length=50, null=True)),
                ('actualhospitalmortality', models.CharField(blank=True, max_length=50, null=True)),
                ('predictedhospitallos', models.FloatField(blank=True, null=True)),
                ('actualhospitallos', models.FloatField(blank=True, null=True)),
                ('preopmi', models.IntegerField(blank=True, null=True)),
                ('preopcardiaccath', models.IntegerField(blank=True, null=True)),
                ('ptcawithin24h', models.IntegerField(blank=True, null=True)),
                ('unabridgedunitlos', models.FloatField(blank=True, null=True)),
                ('unabridgedhosplos', models.FloatField(blank=True, null=True)),
                ('actualventdays', models.FloatField(blank=True, null=True)),
                ('predventdays', models.FloatField(blank=True, null=True)),
                ('unabridgedactualventdays', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'apachepatientresult',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Apachepredvar',
            fields=[
                ('apachepredvarid', models.IntegerField(primary_key=True, serialize=False)),
                ('sicuday', models.SmallIntegerField(blank=True, null=True)),
                ('saps3day1', models.SmallIntegerField(blank=True, null=True)),
                ('saps3today', models.SmallIntegerField(blank=True, null=True)),
                ('saps3yesterday', models.SmallIntegerField(blank=True, null=True)),
                ('gender', models.SmallIntegerField(blank=True, null=True)),
                ('teachtype', models.SmallIntegerField(blank=True, null=True)),
                ('region', models.SmallIntegerField(blank=True, null=True)),
                ('bedcount', models.SmallIntegerField(blank=True, null=True)),
                ('admitsource', models.SmallIntegerField(blank=True, null=True)),
                ('graftcount', models.SmallIntegerField(blank=True, null=True)),
                ('meds', models.SmallIntegerField(blank=True, null=True)),
                ('verbal', models.SmallIntegerField(blank=True, null=True)),
                ('motor', models.SmallIntegerField(blank=True, null=True)),
                ('eyes', models.SmallIntegerField(blank=True, null=True)),
                ('age', models.SmallIntegerField(blank=True, null=True)),
                ('admitdiagnosis', models.CharField(blank=True, max_length=11, null=True)),
                ('thrombolytics', models.SmallIntegerField(blank=True, null=True)),
                ('diedinhospital', models.SmallIntegerField(blank=True, null=True)),
                ('aids', models.SmallIntegerField(blank=True, null=True)),
                ('hepaticfailure', models.SmallIntegerField(blank=True, null=True)),
                ('lymphoma', models.SmallIntegerField(blank=True, null=True)),
                ('metastaticcancer', models.SmallIntegerField(blank=True, null=True)),
                ('leukemia', models.SmallIntegerField(blank=True, null=True)),
                ('immunosuppression', models.SmallIntegerField(blank=True, null=True)),
                ('cirrhosis', models.SmallIntegerField(blank=True, null=True)),
                ('electivesurgery', models.SmallIntegerField(blank=True, null=True)),
                ('activetx', models.SmallIntegerField(blank=True, null=True)),
                ('readmit', models.SmallIntegerField(blank=True, null=True)),
                ('ima', models.SmallIntegerField(blank=True, null=True)),
                ('midur', models.SmallIntegerField(blank=True, null=True)),
                ('ventday1', models.SmallIntegerField(blank=True, null=True)),
                ('oobventday1', models.SmallIntegerField(blank=True, null=True)),
                ('oobintubday1', models.SmallIntegerField(blank=True, null=True)),
                ('diabetes', models.SmallIntegerField(blank=True, null=True)),
                ('managementsystem', models.SmallIntegerField(blank=True, null=True)),
                ('var03hspxlos', models.FloatField(blank=True, null=True)),
                ('pao2', models.FloatField(blank=True, null=True)),
                ('fio2', models.FloatField(blank=True, null=True)),
                ('ejectfx', models.FloatField(blank=True, null=True)),
                ('creatinine', models.FloatField(blank=True, null=True)),
                ('dischargelocation', models.SmallIntegerField(blank=True, null=True)),
                ('visitnumber', models.SmallIntegerField(blank=True, null=True)),
                ('amilocation', models.SmallIntegerField(blank=True, null=True)),
                ('day1meds', models.SmallIntegerField(blank=True, null=True)),
                ('day1verbal', models.SmallIntegerField(blank=True, null=True)),
                ('day1motor', models.SmallIntegerField(blank=True, null=True)),
                ('day1eyes', models.SmallIntegerField(blank=True, null=True)),
                ('day1pao2', models.FloatField(blank=True, null=True)),
                ('day1fio2', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'apachepredvar',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Careplancareprovider',
            fields=[
                ('cplcareprovderid', models.IntegerField(primary_key=True, serialize=False)),
                ('careprovidersaveoffset', models.IntegerField()),
                ('providertype', models.CharField(blank=True, max_length=255, null=True)),
                ('specialty', models.CharField(blank=True, max_length=255, null=True)),
                ('interventioncategory', models.CharField(blank=True, max_length=255, null=True)),
                ('managingphysician', models.CharField(blank=True, max_length=50, null=True)),
                ('activeupondischarge', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'careplancareprovider',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Careplaneol',
            fields=[
                ('cpleolid', models.IntegerField(primary_key=True, serialize=False)),
                ('cpleolsaveoffset', models.IntegerField()),
                ('cpleoldiscussionoffset', models.IntegerField(blank=True, null=True)),
                ('activeupondischarge', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'careplaneol',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Careplangeneral',
            fields=[
                ('cplgeneralid', models.IntegerField(primary_key=True, serialize=False)),
                ('activeupondischarge', models.CharField(max_length=10)),
                ('cplitemoffset', models.IntegerField()),
                ('cplgroup', models.CharField(max_length=255)),
                ('cplitemvalue', models.CharField(blank=True, max_length=1024, null=True)),
            ],
            options={
                'db_table': 'careplangeneral',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Careplangoal',
            fields=[
                ('cplgoalid', models.IntegerField(primary_key=True, serialize=False)),
                ('cplgoaloffset', models.IntegerField()),
                ('cplgoalcategory', models.CharField(blank=True, max_length=255, null=True)),
                ('cplgoalvalue', models.CharField(blank=True, max_length=1000, null=True)),
                ('cplgoalstatus', models.CharField(blank=True, max_length=255, null=True)),
                ('activeupondischarge', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'careplangoal',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Careplaninfectiousdisease',
            fields=[
                ('cplinfectid', models.IntegerField(primary_key=True, serialize=False)),
                ('activeupondischarge', models.CharField(max_length=10)),
                ('cplinfectdiseaseoffset', models.IntegerField()),
                ('infectdiseasesite', models.CharField(blank=True, max_length=64, null=True)),
                ('infectdiseaseassessment', models.CharField(blank=True, max_length=64, null=True)),
                ('responsetotherapy', models.CharField(blank=True, max_length=32, null=True)),
                ('treatment', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'db_table': 'careplaninfectiousdisease',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customlab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customlabid', models.IntegerField()),
                ('labotheroffset', models.IntegerField()),
                ('labothertypeid', models.IntegerField()),
                ('labothername', models.CharField(blank=True, max_length=64, null=True)),
                ('labotherresult', models.CharField(blank=True, max_length=64, null=True)),
                ('labothervaluetext', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'customlab',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('diagnosisid', models.IntegerField(primary_key=True, serialize=False)),
                ('activeupondischarge', models.CharField(blank=True, max_length=64, null=True)),
                ('diagnosisoffset', models.IntegerField()),
                ('diagnosisstring', models.CharField(max_length=200)),
                ('icd9code', models.CharField(blank=True, max_length=100, null=True)),
                ('diagnosispriority', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'diagnosis',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hospitalid', models.IntegerField(primary_key=True, serialize=False)),
                ('numbedscategory', models.CharField(blank=True, max_length=32, null=True)),
                ('teachingstatus', models.BooleanField(blank=True, null=True)),
                ('region', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': 'hospital',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Infusiondrug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('infusiondrugid', models.IntegerField()),
                ('infusionoffset', models.IntegerField()),
                ('drugname', models.CharField(max_length=255)),
                ('drugrate', models.CharField(blank=True, max_length=255, null=True)),
                ('infusionrate', models.CharField(blank=True, max_length=255, null=True)),
                ('drugamount', models.CharField(blank=True, max_length=255, null=True)),
                ('volumeoffluid', models.CharField(blank=True, max_length=255, null=True)),
                ('patientweight', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'infusiondrug',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Intakeoutput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intakeoutputid', models.IntegerField()),
                ('intakeoutputoffset', models.IntegerField()),
                ('intaketotal', models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True)),
                ('outputtotal', models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True)),
                ('dialysistotal', models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True)),
                ('nettotal', models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True)),
                ('intakeoutputentryoffset', models.IntegerField()),
                ('cellpath', models.CharField(blank=True, max_length=500, null=True)),
                ('celllabel', models.CharField(blank=True, max_length=255, null=True)),
                ('cellvaluenumeric', models.DecimalField(decimal_places=4, max_digits=12)),
                ('cellvaluetext', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'intakeoutput',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('labid', models.IntegerField(primary_key=True, serialize=False)),
                ('labresultoffset', models.IntegerField()),
                ('labtypeid', models.DecimalField(decimal_places=0, max_digits=3)),
                ('labname', models.CharField(blank=True, max_length=256, null=True)),
                ('labresult', models.DecimalField(blank=True, decimal_places=4, max_digits=11, null=True)),
                ('labresulttext', models.CharField(blank=True, max_length=255, null=True)),
                ('labmeasurenamesystem', models.CharField(blank=True, max_length=255, null=True)),
                ('labmeasurenameinterface', models.CharField(blank=True, max_length=255, null=True)),
                ('labresultrevisedoffset', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'lab',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicationid', models.IntegerField()),
                ('drugorderoffset', models.IntegerField()),
                ('drugstartoffset', models.IntegerField()),
                ('drugivadmixture', models.CharField(max_length=6)),
                ('drugordercancelled', models.CharField(max_length=6)),
                ('drugname', models.CharField(blank=True, max_length=220, null=True)),
                ('drughiclseqno', models.IntegerField(blank=True, null=True)),
                ('dosage', models.CharField(blank=True, max_length=60, null=True)),
                ('routeadmin', models.CharField(blank=True, max_length=120, null=True)),
                ('frequency', models.CharField(blank=True, max_length=255, null=True)),
                ('loadingdose', models.CharField(max_length=120)),
                ('prn', models.CharField(max_length=6)),
                ('drugstopoffset', models.IntegerField()),
                ('gtc', models.IntegerField()),
            ],
            options={
                'db_table': 'medication',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Microlab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('microlabid', models.IntegerField()),
                ('culturetakenoffset', models.IntegerField()),
                ('culturesite', models.CharField(max_length=255)),
                ('organism', models.CharField(max_length=255)),
                ('antibiotic', models.CharField(blank=True, max_length=255, null=True)),
                ('sensitivitylevel', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'microlab',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noteid', models.IntegerField()),
                ('noteoffset', models.IntegerField()),
                ('noteenteredoffset', models.IntegerField()),
                ('notetype', models.CharField(max_length=50)),
                ('notepath', models.CharField(max_length=255)),
                ('notevalue', models.CharField(blank=True, max_length=150, null=True)),
                ('notetext', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'note',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nurseassessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nurseassessid', models.IntegerField()),
                ('nurseassessoffset', models.IntegerField()),
                ('nurseassessentryoffset', models.IntegerField()),
                ('cellattributepath', models.CharField(max_length=255)),
                ('celllabel', models.CharField(max_length=255)),
                ('cellattribute', models.CharField(max_length=255)),
                ('cellattributevalue', models.CharField(blank=True, max_length=4000, null=True)),
            ],
            options={
                'db_table': 'nurseassessment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nursecare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nursecareid', models.IntegerField()),
                ('celllabel', models.CharField(max_length=255)),
                ('nursecareoffset', models.IntegerField()),
                ('nursecareentryoffset', models.IntegerField()),
                ('cellattributepath', models.CharField(max_length=255)),
                ('cellattribute', models.CharField(max_length=255)),
                ('cellattributevalue', models.CharField(blank=True, max_length=4000, null=True)),
            ],
            options={
                'db_table': 'nursecare',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nursecharting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nursingchartid', models.BigIntegerField()),
                ('nursingchartoffset', models.IntegerField()),
                ('nursingchartentryoffset', models.IntegerField()),
                ('nursingchartcelltypecat', models.CharField(max_length=255)),
                ('nursingchartcelltypevallabel', models.CharField(blank=True, max_length=255, null=True)),
                ('nursingchartcelltypevalname', models.CharField(blank=True, max_length=255, null=True)),
                ('nursingchartvalue', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'nursecharting',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pasthistory',
            fields=[
                ('pasthistoryid', models.IntegerField(primary_key=True, serialize=False)),
                ('pasthistoryoffset', models.IntegerField()),
                ('pasthistoryenteredoffset', models.IntegerField()),
                ('pasthistorynotetype', models.CharField(blank=True, max_length=40, null=True)),
                ('pasthistorypath', models.CharField(max_length=255)),
                ('pasthistoryvalue', models.CharField(blank=True, max_length=100, null=True)),
                ('pasthistoryvaluetext', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'pasthistory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patientunitstayid', models.IntegerField(primary_key=True, serialize=False)),
                ('patienthealthsystemstayid', models.IntegerField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=25, null=True)),
                ('age', models.CharField(blank=True, max_length=10, null=True)),
                ('ethnicity', models.CharField(blank=True, max_length=50, null=True)),
                ('wardid', models.IntegerField(blank=True, null=True)),
                ('apacheadmissiondx', models.CharField(blank=True, max_length=1000, null=True)),
                ('admissionheight', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('hospitaladmittime24', models.CharField(blank=True, max_length=8, null=True)),
                ('hospitaladmitoffset', models.IntegerField(blank=True, null=True)),
                ('hospitaladmitsource', models.CharField(blank=True, max_length=30, null=True)),
                ('hospitaldischargeyear', models.SmallIntegerField(blank=True, null=True)),
                ('hospitaldischargetime24', models.CharField(blank=True, max_length=8, null=True)),
                ('hospitaldischargeoffset', models.IntegerField(blank=True, null=True)),
                ('hospitaldischargelocation', models.CharField(blank=True, max_length=100, null=True)),
                ('hospitaldischargestatus', models.CharField(blank=True, max_length=10, null=True)),
                ('unittype', models.CharField(blank=True, max_length=50, null=True)),
                ('unitadmittime24', models.CharField(blank=True, max_length=8, null=True)),
                ('unitadmitsource', models.CharField(blank=True, max_length=100, null=True)),
                ('unitvisitnumber', models.IntegerField(blank=True, null=True)),
                ('unitstaytype', models.CharField(blank=True, max_length=15, null=True)),
                ('admissionweight', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('dischargeweight', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('unitdischargetime24', models.CharField(blank=True, max_length=8, null=True)),
                ('unitdischargeoffset', models.IntegerField(blank=True, null=True)),
                ('unitdischargelocation', models.CharField(blank=True, max_length=100, null=True)),
                ('unitdischargestatus', models.CharField(blank=True, max_length=10, null=True)),
                ('uniquepid', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'patient',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Physicalexam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physicalexamid', models.IntegerField(blank=True, null=True)),
                ('physicalexamoffset', models.IntegerField()),
                ('physicalexampath', models.CharField(max_length=255)),
                ('physicalexamvalue', models.CharField(blank=True, max_length=100, null=True)),
                ('physicalexamtext', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'physicalexam',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Respiratorycare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respcareid', models.IntegerField(blank=True, null=True)),
                ('respcarestatusoffset', models.IntegerField(blank=True, null=True)),
                ('currenthistoryseqnum', models.IntegerField(blank=True, null=True)),
                ('airwaytype', models.CharField(blank=True, max_length=30, null=True)),
                ('airwaysize', models.CharField(blank=True, max_length=10, null=True)),
                ('airwayposition', models.CharField(blank=True, max_length=32, null=True)),
                ('cuffpressure', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('ventstartoffset', models.IntegerField(blank=True, null=True)),
                ('ventendoffset', models.IntegerField(blank=True, null=True)),
                ('priorventstartoffset', models.IntegerField(blank=True, null=True)),
                ('priorventendoffset', models.IntegerField(blank=True, null=True)),
                ('apneaparams', models.CharField(blank=True, max_length=80, null=True)),
                ('lowexhmvlimit', models.DecimalField(blank=True, decimal_places=4, max_digits=11, null=True)),
                ('hiexhmvlimit', models.DecimalField(blank=True, decimal_places=4, max_digits=11, null=True)),
                ('lowexhtvlimit', models.DecimalField(blank=True, decimal_places=4, max_digits=11, null=True)),
                ('hipeakpreslimit', models.DecimalField(blank=True, decimal_places=4, max_digits=11, null=True)),
                ('lowpeakpreslimit', models.DecimalField(blank=True, decimal_places=4, max_digits=11, null=True)),
                ('hirespratelimit', models.DecimalField(blank=True, decimal_places=4, max_digits=11, null=True)),
                ('lowrespratelimit', models.DecimalField(blank=True, decimal_places=4, max_digits=11, null=True)),
                ('sighpreslimit', models.DecimalField(blank=True, decimal_places=4, max_digits=11, null=True)),
                ('lowironoxlimit', models.DecimalField(blank=True, decimal_places=4, max_digits=11, null=True)),
                ('highironoxlimit', models.DecimalField(blank=True, decimal_places=4, max_digits=11, null=True)),
                ('meanairwaypreslimit', models.DecimalField(blank=True, decimal_places=4, max_digits=11, null=True)),
                ('peeplimit', models.DecimalField(blank=True, decimal_places=4, max_digits=11, null=True)),
                ('cpaplimit', models.DecimalField(blank=True, decimal_places=4, max_digits=11, null=True)),
                ('setapneainterval', models.CharField(blank=True, max_length=80, null=True)),
                ('setapneatv', models.CharField(blank=True, max_length=80, null=True)),
                ('setapneaippeephigh', models.CharField(blank=True, max_length=80, null=True)),
                ('setapnearr', models.CharField(blank=True, max_length=80, null=True)),
                ('setapneapeakflow', models.CharField(blank=True, max_length=80, null=True)),
                ('setapneainsptime', models.CharField(blank=True, max_length=80, null=True)),
                ('setapneaie', models.CharField(blank=True, max_length=80, null=True)),
                ('setapneafio2', models.CharField(blank=True, max_length=80, null=True)),
            ],
            options={
                'db_table': 'respiratorycare',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Respiratorycharting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respchartid', models.IntegerField(blank=True, null=True)),
                ('respchartoffset', models.IntegerField(blank=True, null=True)),
                ('respchartentryoffset', models.IntegerField(blank=True, null=True)),
                ('respcharttypecat', models.CharField(blank=True, max_length=255, null=True)),
                ('respchartvaluelabel', models.CharField(blank=True, max_length=255, null=True)),
                ('respchartvalue', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'respiratorycharting',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('treatmentid', models.IntegerField(primary_key=True, serialize=False)),
                ('treatmentoffset', models.IntegerField(blank=True, null=True)),
                ('treatmentstring', models.CharField(blank=True, max_length=200, null=True)),
                ('activeupondischarge', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'treatment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vitalaperiodic',
            fields=[
                ('vitalaperiodicid', models.IntegerField(primary_key=True, serialize=False)),
                ('observationoffset', models.IntegerField()),
                ('noninvasivesystolic', models.FloatField(blank=True, null=True)),
                ('noninvasivediastolic', models.FloatField(blank=True, null=True)),
                ('noninvasivemean', models.FloatField(blank=True, null=True)),
                ('paop', models.FloatField(blank=True, null=True)),
                ('cardiacoutput', models.FloatField(blank=True, null=True)),
                ('cardiacinput', models.FloatField(blank=True, null=True)),
                ('svr', models.FloatField(blank=True, null=True)),
                ('svri', models.FloatField(blank=True, null=True)),
                ('pvr', models.FloatField(blank=True, null=True)),
                ('pvri', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'vitalaperiodic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vitalperiodic',
            fields=[
                ('vitalperiodicid', models.BigIntegerField(primary_key=True, serialize=False)),
                ('observationoffset', models.IntegerField(blank=True, null=True)),
                ('temperature', models.DecimalField(blank=True, decimal_places=4, max_digits=11, null=True)),
                ('sao2', models.IntegerField(blank=True, null=True)),
                ('heartrate', models.IntegerField(blank=True, null=True)),
                ('respiration', models.IntegerField(blank=True, null=True)),
                ('cvp', models.IntegerField(blank=True, null=True)),
                ('etco2', models.IntegerField(blank=True, null=True)),
                ('systemicsystolic', models.IntegerField(blank=True, null=True)),
                ('systemicdiastolic', models.IntegerField(blank=True, null=True)),
                ('systemicmean', models.IntegerField(blank=True, null=True)),
                ('pasystolic', models.IntegerField(blank=True, null=True)),
                ('padiastolic', models.IntegerField(blank=True, null=True)),
                ('pamean', models.IntegerField(blank=True, null=True)),
                ('st1', models.FloatField(blank=True, null=True)),
                ('st2', models.FloatField(blank=True, null=True)),
                ('st3', models.FloatField(blank=True, null=True)),
                ('icp', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'vitalperiodic',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]