from __future__ import unicode_literals
from django.shortcuts import render
import json,os
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
import operator

# Create your views here.
@csrf_exempt
def PatientRegister(request):
    aadhaarid = request.POST.get('aadhaarid')
    name = request.POST.get('name')
    dob = request.POST.get('dob')
    address = request.POST.get('address')
    gender = request.POST.get('gender')
    contact = request.POST.get('contact')
    patient = Patients()
    patient.aadhaarid = aadhaarid
    patient.name = name
    patient.dob = dob
    patient.address = address
    patient.gender = gender
    patient.contact = contact
    patient.save()
    response_array = {}
    response_array['status'] = 1
    response_array['data'] = 'success'
    return HttpResponse(json.dumps(response_array), status=200, content_type="application/json")

@csrf_exempt
def FetchPatientDetails(request):
    aadhaarid = request.GET.get('aadhaarid')
    patient = Patients.objects.get(aadhaarid=aadhaarid)
    response_array = {}
    response_array['status'] = 1
    response_array['data'] = {}
    response_array['data']['aadhaarid'] = patient.aadhaarid
    response_array['data']['name'] = patient.name
    response_array['data']['dob'] = patient.dob
    response_array['data']['address'] = patient.address
    response_array['data']['gender'] = patient.gender
    response_array['data']['contact'] = patient.contact
    return HttpResponse(json.dumps(response_array), status=200, content_type="application/json")

##TODO:TEST
@csrf_exempt
def GetAllPatientRecords(request):
    aadhaarid = request.GET.get('aadhaarid')
    patientRecord = Patientrecords.objects.values().get(patient=Patients.objects.get(aadhaarid=aadhaarid))

    response_array = {}
    response_array['status'] = 1
    response_array['data'] = []
    for patientRecord in patientRecord:
        patientRecordObj = {}
        patientRecordObj['symptoms'] = patientRecord.symptoms
        patientRecordObj['diagnosis'] = patientRecord.diagnosis
        patientRecordObj['addedby'] = patientRecord.addedby
        patientRecordObj['attatchmentlink'] = patientRecord.attatchmentlink
        patientRecordObj['createdat'] = patientRecord.createdat
        patientRecordObj['createdon'] = patientRecord.createdon
        patientRecordObj['id'] = patientRecord.id
        response_array['data'].append(patientRecordObj)
    return HttpResponse(json.dumps(response_array), status=200, content_type="application/json")

##TODO : TEST
@csrf_exempt
def CreateNewPatientRecord(request):
    aadhaarid = request.POST.get('aadhaarid')
    patient = Patients.objects.get(aadhaarid=aadhaarid)
    symptoms = request.POST.get('symptoms')
    diagnosis = request.POST.get('diagnosis')
    addedby = request.POST.get('addedby')
    attatchmentlink = request.POST.get('attatchmentlink')
    createdat = request.POST.get('createdat')
    createdon = request.POST.get('createdon')
    patientRecord = Patientrecords()
    patientRecord.patient = patient
    patientRecord.symptoms = symptoms
    patientRecord.diagnosis = diagnosis
    patientRecord.addedby = addedby
    patientRecord.attatchmentlink = attatchmentlink
    patientRecord.createdat = createdat
    patientRecord.createdon = createdon
    patientRecord.save()

    response_array = {}
    response_array['status'] = 1
    response_array['data'] = 'success'
    return HttpResponse(json.dumps(response_array), status=200, content_type="application/json")

##TODO : add closedAt flag into db ???
##TODO : TEST
@csrf_exempt
def CreateNewVidChatRoom(request):
    aadhaarid = request.POST.get('aadhaarid')
    patient = Patients.objects.get(aadhaarid=aadhaarid)
    createdat = request.POST.get('createdat')
    #doctor = Doctors.objects.get( = )
    videorecords = Videorecords()
    videorecords.patient = patient
    #videorecords.doctor = doctor
    videorecords.createdat = createdat
    videorecords.save()

    response_array = {}
    response_array['status'] = 1
    response_array['data'] = 'success'
    return HttpResponse(json.dumps(response_array), status=200, content_type="application/json")

@csrf_exempt
def SearchDoctor(request):
    name = request.GET.get('name')
    doctor = Doctors.objects.values().get(name=name)

    response_array = {}
    response_array['status'] = 1
    response_array['data'] = []
    for doctor in doctor:
        doctorObj = {}
        doctorObj['available'] = doctor.available
        doctorObj['name'] = doctor.name
        doctorObj['speciality'] = doctor.speciality
        doctorObj['currentlocation'] = doctor.currentlocation
        response_array['data'].append(doctorObj)
    return HttpResponse(json.dumps(response_array), status=200, content_type="application/json")

@csrf_exempt
def SearchDoctorBySpeciality(request):
    speciality = request.GET.get('speciality')
    doctor = Doctors.objects.get(speciality=speciality)

    response_array = {}
    response_array['status'] = 1
    response_array['data'] = []
    for doctor in doctor:
        doctorObj = {}
        doctorObj['available'] = doctor.available
        doctorObj['name'] = doctor.name
        doctorObj['speciality'] = doctor.speciality
        doctorObj['currentlocation'] = doctor.currentlocation
        response_array['data'].append(doctorObj)
    return HttpResponse(json.dumps(response_array), status=200, content_type="application/json")

##TODO: add ForeignKey relation in db for currentlocation and hospital-> id
@csrf_exempt
def SearchDoctorByHospitalName(request):
    currentlocation = request.GET.get('currenthospital')
    doctor = Doctors.objects.values().get(currentlocation=Hospitals.objects.get(name=currentlocation))

    response_array = {}
    response_array['status'] = 1
    response_array['data'] = []
    for doctor in doctor:
        doctorObj = {}
        doctorObj['available'] = doctor.available
        doctorObj['name'] = doctor.name
        doctorObj['speciality'] = doctor.speciality
        doctorObj['currentlocation'] = doctor.currentlocation
        response_array['data'].append(doctorObj)
    return HttpResponse(json.dumps(response_array), status=200, content_type="application/json")

@csrf_exempt
def EmergencyDoctorSearch(request):
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    speciality = request.GET.get('speciality')
    hospitals = Hospitals.objects.all()
    noOfClosestDoctors = 5

    hospitalDistDict = {}
    for hospital in hospitals:
        location = hospital.location
        latitudeDb = location.split(',')[0]
        longitudeDb = location.split(',')[1]
        sqDist = ((latitudeDb - latitude)**2 +(longitudeDb - longitude)**2)
        hospitalDistDict[hospital.name] = sqDist
    sorted_hospitals = sorted(hospitalDistDict.items(), key=operator.itemgetter(1))

    response_array = {}
    response_array['status'] = 1
    response_array['data'] = []
    for i in range(noOfClosestDoctors):
        doctor = Doctors.objects.get(currentlocation=Hospitals.objects.get(name=sorted_hospitals[sorted_hospitals.keys()[i]]))
        doctorObj = {}
        doctorObj['available'] = doctor.available
        doctorObj['name'] = doctor.name
        doctorObj['speciality'] = doctor.speciality
        doctorObj['currentlocation'] = doctor.currentlocation
        response_array['data'].append(doctorObj)
    return HttpResponse(json.dumps(response_array), status=200, content_type="application/json")
