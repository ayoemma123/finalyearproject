from django.forms import ModelForm
from .models import Cad, Hf

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput

from django import forms

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):

    username = forms.CharField(widget = TextInput())
    password = forms.CharField(widget = PasswordInput())


class CadForm(ModelForm):

    class Meta:

        model = Cad
        fields = '__all__'

class HfForm(ModelForm):

    class Meta:
        
        model = Hf
        fields = '__all__'

class HFPredictionForm(forms.Form):
    age = forms.IntegerField(label='Age')
    anaemia = forms.ChoiceField(label='anaemia', choices=[(0, 'Type 1'), (1, 'Type 2')])
    creatinine_phosphokinase = forms.IntegerField(label='creatinine_phosphokinase: Enter value from 0-6000')
    diabetes = forms.ChoiceField(label='diabetes', choices=[(0, 'Type 1'), (1, 'Type 2')])
    ejection_fraction = forms.IntegerField(label='ejection_fraction: Enter value from 20 - 70')
    high_blood_pressure = forms.ChoiceField(label=' high_blood_pressure', choices=[(0, 'No'), (1, 'Yes')])
    platelets = forms.IntegerField(label='platelets: Enter values from 40,000 - 300,000')
    serum_creatinine = forms.FloatField(label='serum_creatinine: Enter values from 1.0 - 3.0')
    serum_sodium = forms.IntegerField(label='serum_sodium: Enter values from 100 - 150')
    sex = forms.ChoiceField(label='Sex', choices=[(0, 'Female'), (1, 'Male')])
    smoking = forms.ChoiceField(label='Do you smoke', choices=[(0, 'No'), (1, 'Yes')])
    time = forms.IntegerField(label='time: Enter time from 1s - 300s')
    
class PredictionForm(forms.Form):
    age = forms.IntegerField(label='Age')
    sex = forms.ChoiceField(label='Sex', choices=[(0, 'Female'), (1, 'Male')])
    cp = forms.ChoiceField(label='Chest Pain Type', choices=[(0, 'Type 1'), (1, 'Type 2'), (2, ' Type 3'), (3, 'Type 4')])
    trestbps = forms.IntegerField(label='Resting Blood Pressure: Enter Value From 100 - 200')
    cholesterol = forms.IntegerField(label='Cholesterol: Enter value from 150 - 300')
    fbs = forms.ChoiceField(label='Fasting Blood Sugar', choices=[(0, 'Type 1'), (1, 'Type 2')])
    restecg = forms.ChoiceField(label='Resting Electrocardiographic Results', choices=[(0, 'Result 1'), (1, 'Result 2')])
    thalach = forms.IntegerField(label='Maximum Heart Rate Achieved: Enter value from 100 - 200')
    exang =  forms.ChoiceField(label='Exercise Induced Angina', choices=[(0, 'Type 1'), (1, 'Type 2')])
    oldpeak =  forms.FloatField(label='ST Depression Induced by Exercise: Enter values from 0.0 - 5.0')
    slope =  forms.ChoiceField(label='Slope of the Peak Exercise ST Segment', choices=[(0, 'Type 1'), (1, 'Type 2'), (2, 'Type 3'), (3, ' Type 4')])
    ca =  forms.ChoiceField(label='Number of Major Vessels Colored by Fluoroscopy', choices=[ (1, 'Type 1'), (2, 'Type 2'), (3, 'Type 3')])
    thal = forms.ChoiceField(label='Thalassemia', choices=[(0, 'No'), (1, 'Yes')])


