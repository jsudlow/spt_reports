from django.contrib import admin
from django.core.urlresolvers import reverse

# Register your models here.
from .models import Patient,Physician,SpeechEvaluationReport,Test,TestScore

class ScoreInline(admin.TabularInline):
    model = TestScore
    extra = 1
class TestAdmin(admin.ModelAdmin):
  inlines = [ScoreInline]



class SpeechEvaluationReportAdmin(admin.ModelAdmin):
  list_display = ['patient','date_of_visit','my_url_field']
  fieldsets = [
      (None,           {'fields': ['patient','location','report_type','date_of_visit','diagnosis','identifying_information_and_referral','parent_concern','background_information','pregnancy_and_birth','medical','developmental','family_social','education','hearing','cranial_nerve_exam']}),
      ('Articulation', {'fields': ['articulation'], 'classes': ['collapse']}),
      ('Initial Language Evaluation', {'fields': ['initial_language_evaluation'], 'classes': ['collapse']}),
      ('Speech-Language Re-Evaluation and Progress(for six month assessment)', {'fields': ['speech_language_reevaluation_and_progress'], 'classes': ['collapse']}),
      ('Language Sample', {'fields': ['language_sample'], 'classes': ['collapse']}),
      (None, {'fields': ['voice_and_fluency','clinical_impressions_and_recommendations','referrals_and_follow_up','long_term_goals','short_term_goals','statement_of_medical_neccessity','electronic_signature']})
  ]
  

  def my_url_field(self, obj):
      #link = "<a href='http://localhost:8000/reports/generate_speech_eval_report/" + str(obj.id) +"/'>Generate Report</a>" 
      link = "<a href='" + reverse('generate_speech_eval_report',args=[obj.id]) + "' target='_blank'>Generate Report</a>"
      return link
  my_url_field.allow_tags = True
  my_url_field.short_description = 'Generate Report'
  
  

admin.site.register(Patient)
admin.site.register(Test,TestAdmin)
admin.site.register(TestScore)

admin.site.register(Physician)
admin.site.register(SpeechEvaluationReport,SpeechEvaluationReportAdmin)
