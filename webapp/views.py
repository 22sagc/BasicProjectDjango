import json

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from myproject import settings
from django.views.decorators.csrf import csrf_exempt
from webapp.models import patient



def index(request):
    return render(request, 'landing_page.html')

@csrf_exempt
def patient_registrations_landing(request):
    return render(request, 'registration_page.html')


import pdb
@csrf_exempt
def patient_registrations(request):
    try:
        data = {}
        patientObj = patient(
            name=request.POST.get('name'),
            mobile=request.POST.get('mobile'),
            address=request.POST.get('address'),
            age=request.POST.get('age'),
            gender=request.POST.get('gender'),
        )
        patientObj.save()

        data = {'success': 'true'}
        return HttpResponse(json.dumps(data), content_type='application/json')

    except Exception as e:
        data = {'success': 'false'}
    return HttpResponse(json.dumps(data), content_type='application/json')


@csrf_exempt
def patient_details(request):
    patientObj = patient.objects.all()

    data = {'patientObj':patientObj}
    return render(request, 'patient_details.html', data)