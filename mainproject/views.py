from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm, PredictionForm, HFPredictionForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login as auth_login, logout
import joblib
import numpy as np
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)

# Load the models once at startup
cad_model = joblib.load('CADAI.pkl')  # Ensure the path is correct
hf_model = joblib.load('HF.pkl')  # Ensure the path is correct

def predict(model, features):
    # Convert features to numeric values
    features = np.array([float(x) for x in features]).reshape(1, -1)
    prediction = model.predict(features)
    return prediction[0]

@login_required(login_url='login')
def CAD(request):
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            features = [
                form.cleaned_data['age'],
                form.cleaned_data['sex'],
                form.cleaned_data['cp'],
                form.cleaned_data['trestbps'],
                form.cleaned_data['cholesterol'],
                form.cleaned_data['fbs'],
                form.cleaned_data['restecg'],
                form.cleaned_data['thalach'],
                form.cleaned_data['exang'],
                form.cleaned_data['oldpeak'],
                form.cleaned_data['slope'],
                form.cleaned_data['ca'],
                form.cleaned_data['thal'],
            ]
            print(f"Features: {features}")  # Debugging statement
            result = predict(cad_model, features)
            print(f"Prediction Result: {result}")  # Debugging statement
            
            pre = 'The doctor wants to see you in his office. If you have any questions, you can contact him at emmanuel.olulana@stu.cu.edu.ng.'

            send_email_with_predictions(pre)
            return render(request, 'result.html', {'result': result})
    else:
        form = PredictionForm()
    return render(request, 'CAD.html', {'form': form})

@login_required(login_url='login')
def HEARTFAILURE(request):
    if request.method == 'POST':
        form = HFPredictionForm(request.POST)
        if form.is_valid():
            features = [
                form.cleaned_data['age'],
                form.cleaned_data['anaemia'],
                form.cleaned_data['creatinine_phosphokinase'],
                form.cleaned_data['diabetes'],
                form.cleaned_data['ejection_fraction'],
                form.cleaned_data['high_blood_pressure'],
                form.cleaned_data['platelets'],
                form.cleaned_data['serum_creatinine'],
                form.cleaned_data['serum_sodium'],
                form.cleaned_data['sex'],
                form.cleaned_data['smoking'],
                form.cleaned_data['time'],
            ]
            print(f"Features: {features}")  # Debugging statement
            result = predict(hf_model, features)
        
            pre = 'The doctor wants to see you in his office. If you have any questions, you can contact him at emmanuel.olulana@stu.cu.edu.ng.'

            print(f"Prediction Result: {result}")  # Debugging statement


            send_email_with_predictions(pre)
            return render(request, 'HFresultS.html', {'result': result})
    else:
        form = HFPredictionForm()
    return render(request, 'HEARTFAILURE.html', {'form': form})

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('dashboard')
    context = {'form': form}
    return render(request, 'login.html', context=context)

def home(request):
    return render(request, 'home.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'registration.html', context=context)

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def send_email_with_predictions(predictions):
    subject = 'Predictions'
    message = f'Predictions: {predictions}'
    from_email = 'olulanaayodeji98@gmail.com'
    to_email = ['emmanuel.olulana@stu.cu.edu.ng', 'emmanuelolulana72@gmail.com']
    try:
        send_mail(subject, message, from_email, to_email)
        logger.info('Email sent successfully')
    except Exception as e:
        logger.error(f'Failed to send email: {e}')
