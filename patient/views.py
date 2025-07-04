from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum,Q
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from datetime import date, timedelta
from django.core.mail import send_mail
from django.contrib.auth.models import User
from blood import forms as bforms
from blood import models as bmodels


def patient_signup_view(request):
    userForm=forms.PatientUserForm()
    patientForm=forms.PatientForm()
    mydict={'userForm':userForm,'patientForm':patientForm}
    if request.method=='POST':
        userForm=forms.PatientUserForm(request.POST)
        patientForm=forms.PatientForm(request.POST,request.FILES)
        if userForm.is_valid() and patientForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            patient=patientForm.save(commit=False)
            patient.user=user
            patient.bloodgroup=patientForm.cleaned_data['bloodgroup']
            patient.save()
            my_patient_group = Group.objects.get_or_create(name='PATIENT')
            my_patient_group[0].user_set.add(user)
        return HttpResponseRedirect('patientlogin')
    return render(request,'patient/patientsignup.html',context=mydict)

def patient_dashboard_view(request):
    patient= models.Patient.objects.get(user_id=request.user.id)
    dict={
        'requestpending': bmodels.BloodRequest.objects.all().filter(request_by_patient=patient).filter(status='Pending').count(),
        'requestapproved': bmodels.BloodRequest.objects.all().filter(request_by_patient=patient).filter(status='Approved').count(),
        'requestmade': bmodels.BloodRequest.objects.all().filter(request_by_patient=patient).count(),
        'requestrejected': bmodels.BloodRequest.objects.all().filter(request_by_patient=patient).filter(status='Rejected').count(),

    }
   
    return render(request,'patient/patient_dashboard.html',context=dict)

def make_request_view(request):
    request_form=bforms.RequestForm()
    if request.method=='POST':
        request_form=bforms.RequestForm(request.POST)
        if request_form.is_valid():
            blood_request=request_form.save(commit=False)
            blood_request.bloodgroup=request_form.cleaned_data['bloodgroup']
            patient= models.Patient.objects.get(user_id=request.user.id)
            blood_request.request_by_patient=patient
            blood_request.save()
            return HttpResponseRedirect('my-request')  
    return render(request,'patient/makerequest.html',{'request_form':request_form})

def my_request_view(request):
    patient= models.Patient.objects.get(user_id=request.user.id)
    blood_request=bmodels.BloodRequest.objects.all().filter(request_by_patient=patient)
    return render(request,'patient/my_request.html',{'blood_request':blood_request})


import sys
import subprocess
from django.shortcuts import render
from django.http import HttpResponse

def run_chatbot(request):
    chatbot_script = 'templates/patient/chatbot.py'  # Path to the chatbot.py script

    try:
        # Run the chatbot script using subprocess
        subprocess.Popen([sys.executable, chatbot_script])
        success_message = "Let's Talk!"
        html_response = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Chatbot Started</title>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
            <style>
                body {{
                    background-color: #f9f9f9; /* Light gray background */
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding-top: 50px;
                }}
                .success-message {{
                    background-color: #4CAF50; /* Green */
                    color: white;
                    padding: 20px;
                    border-radius: 10px;
                    margin: auto;
                    width: 50%;
                    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
                    animation: fadeIn 0.5s ease;
                }}
                @keyframes fadeIn {{
                    from {{ opacity: 0; }}
                    to {{ opacity: 1; }}
                }}
                .fas {{
                    margin-right: 10px;
                }}
            </style>
        </head>
        <body>
            <div class="success-message">
                <i class="fas fa-check-circle"></i>
                <h1>Hello!</h1>
                <p>{success_message}</p>
            </div>
        </body>
        </html>
        """
        return HttpResponse(html_response)
    except Exception as e:
        error_message = f"Error: {e}"
        html_response = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Error</title>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
            <style>
                body {{
                    background-color: #f9f9f9; /* Light gray background */
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding-top: 50px;
                }}
                .error-message {{
                    background-color: #f44336; /* Red */
                    color: white;
                    padding: 20px;
                    border-radius: 10px;
                    margin: auto;
                    width: 50%;
                    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
                    animation: fadeIn 0.5s ease;
                }}
                @keyframes fadeIn {{
                    from {{ opacity: 0; }}
                    to {{ opacity: 1; }}
                }}
                .fas {{
                    margin-right: 10px;
                }}
            </style>
        </head>
        <body>
            <div class="error-message">
                <i class="fas fa-exclamation-circle"></i>
                <h1>Error!</h1>
                <p>{error_message}</p>
            </div>
        </body>
        </html>
        """
        return HttpResponse(html_response)


