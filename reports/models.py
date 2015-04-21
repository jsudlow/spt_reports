from django.db import models
from ckeditor.fields import RichTextField




# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    account_number = models.IntegerField()
    date_of_birth = models.DateField()
    clinician = models.CharField(max_length=30)
    supervising_clinician = models.CharField(max_length=30)
    payor = models.CharField(max_length=30)
    pol_claim_number = models.CharField(max_length=30)
    ssn = models.CharField(max_length=20)
    visits = models.IntegerField()
    chronological_age = models.IntegerField()
    adjusted_age = models.IntegerField()
    referral_physician = models.CharField(max_length=100)
    referral_physician_phone = models.CharField(max_length=20)
    referral_physician_fax = models.CharField(max_length=20)
    pediatrician = models.CharField(max_length=100)
    pediatrician_phone = models.CharField(max_length=20)
    pediatrician_fax = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Test(models.Model):
    test_name = models.CharField(max_length=200)
    patient = models.ForeignKey(Patient)
    
    def __str__(self):
        return self.test_name

class TestScore(models.Model):
    test = models.ForeignKey(Test)
    score_text = models.CharField(max_length=200)
    score_value = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.score_text)

class Physician(models.Model):
    patient = models.ForeignKey(Patient)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    doctor_type = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    fax = models.CharField(max_length=30)

class SpeechEvaluationReport(models.Model):
    patient = models.ForeignKey(Patient)
    date_of_visit = models.DateField()
    diagnosis = models.CharField(max_length=200)
    identifying_information_and_referral = RichTextField()
    parent_concern = RichTextField()
    background_information = RichTextField()
    pregnancy_and_birth = RichTextField()
    medical = RichTextField()
    developmental = RichTextField()
    family_social = RichTextField()
    education = RichTextField()
    hearing = RichTextField()
    cranial_nerve_exam = RichTextField()
    articulation = RichTextField()
    language_evaluation = RichTextField()
    language_sample = RichTextField()
    voice_and_fluency = RichTextField()
    summary_and_recommendations = RichTextField()
    electronic_signature = RichTextField()
    
    
    def __str__(self):
        return self.patient.first_name + " " + self.patient.last_name + " " + str(self.date_of_visit)



    
