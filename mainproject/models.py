from django.db import models


class Cad(models.Model):

    age = models.CharField(max_length = 85)
    sex = models.CharField(max_length = 85)
    cp = models.CharField(max_length = 85)
    trestbps = models.CharField(max_length = 85) 
    chol = models.CharField(max_length = 85)
    fbs = models.CharField(max_length = 85)
    restecg = models.CharField(max_length = 85)
    thalach = models.CharField(max_length = 85)
    exang = models.CharField(max_length = 85)
    oldpeak = models.CharField(max_length = 85)
    slope = models.CharField(max_length = 85)
    ca = models.CharField(max_length = 85)
    thal = models.CharField(max_length = 85)

    

class Hf(models.Model):

    age = models.CharField(max_length = 85)
    anaemia = models.CharField(max_length = 85)
    cholcreatinine_phosphokinase = models.CharField(max_length = 85)
    diabetes = models.CharField(max_length = 85)
    ejection_fraction = models.CharField(max_length = 85)
    high_blood_pressure = models.CharField(max_length = 85)
    platelets = models.CharField(max_length = 85)
    serum_creatinine = models.CharField(max_length = 85)
    serum_sodium = models.CharField(max_length = 85)
    sex = models.CharField(max_length = 85)
    smoking = models.CharField(max_length = 85)
    time = models.CharField(max_length = 85)
    DEATHEVENT = models.CharField(max_length = 85)
    

