from django.db import models
from ckeditor.fields import RichTextField

LOCATION_CHOICES = (
        ('Aurora', 'Aurora'),
        ('Naperville North', 'Naperville North'),
        ('Naperville Central', 'Naperville Central')
    )
SPEECH_EVAL_REPORT_TITLES = (
        ('Initial Speech-Language Evaluation Report', 'Initial Speech-Language Evaluation Report'),
        ('Speech-Language Re-evaluation Report', 'Speech-Language Re-evaluation Report'),
    )

OCCUPATIONAL_EVAL_REPORT_TITLES = (
        ('Initial Occupational-Language Evaluation Report', 'Initial Occupational-Language Evaluation Report'),
        ('Occupational-Language Re-evaluation Report', 'Occupational-Language Re-evaluation Report'),
    )
# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    clinician = models.CharField(max_length=30)
    supervising_clinician = models.CharField(max_length=30,blank=True)
    chronological_age = models.DecimalField(max_digits=5, decimal_places=2,blank=True,null=True)
    adjusted_age = models.IntegerField(blank=True,null=True)
    referral_physician = models.CharField(max_length=100)
    referral_physician_phone = models.CharField(max_length=20)
    referral_physician_fax = models.CharField(max_length=20)
    pediatrician = models.CharField(max_length=100,blank=True)
    pediatrician_phone = models.CharField(max_length=20,blank=True)
    pediatrician_fax = models.CharField(max_length=20,blank=True)

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
    location = models.CharField(max_length=200, choices=LOCATION_CHOICES)
    report_type = models.CharField(max_length=200, choices=SPEECH_EVAL_REPORT_TITLES)
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
    behavioral_observation = RichTextField(blank=True)
    cranial_nerve_exam = RichTextField()
    articulation = RichTextField(blank=True)
    language = RichTextField(blank=True)
    speech_language_progress = RichTextField(blank=True)
    language_sample = RichTextField(blank=True)
    voice_and_fluency = RichTextField()
    clinical_impressions_and_recommendations = RichTextField()
    referrals_and_follow_up = RichTextField()
    long_term_goals = RichTextField()
    short_term_goals = RichTextField()
    statement_of_medical_neccessity = RichTextField()
    electronic_signature = RichTextField()
    
    
    def __str__(self):
        return self.patient.first_name + " " + self.patient.last_name + " " + str(self.date_of_visit)
		
class OccupationalEvaluationReport(models.Model):
    patient = models.ForeignKey(Patient)
    date_of_visit = models.DateField()
    location = models.CharField(max_length=200, choices=LOCATION_CHOICES)
    report_type = models.CharField(max_length=200, choices=OCCUPATIONAL_EVAL_REPORT_TITLES)
    diagnosis = models.CharField(max_length=200)
    identifying_information_and_referral = RichTextField()
    parent_concern = RichTextField()
    background_information = RichTextField()
    pregnancy_and_birth = RichTextField()
    medical = RichTextField()
    developmental = RichTextField()
    family_social = RichTextField()
    education = RichTextField()
    activities_of_daily_living = RichTextField()
    strength = RichTextField()
    muscle_tone = RichTextField()
    fine_motor_skills = RichTextField()
    visual_motor_skills = RichTextField()
    sensory_processing = RichTextField()
    adaptive_skills = RichTextField()
    clinical_impressions_and_recommendations = RichTextField()
    referrals_and_follow_up = RichTextField()
    long_term_goals = RichTextField()
    short_term_goals = RichTextField()
    statement_of_medical_neccessity = RichTextField()
    electronic_signature = RichTextField()
	
    def __str__(self):
        return self.patient.first_name + " " + self.patient.last_name + " " + str(self.date_of_visit)
	
	



    
