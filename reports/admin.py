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
  

  def my_url_field(self, obj):
      #link = "<a href='http://localhost:8000/reports/generate_speech_eval_report/" + str(obj.id) +"/'>Generate Report</a>" 
      link = "<a href='" + reverse('generate_speech_eval_report',args=[obj.id]) +"'>Generate Report</a>"
      return link
  my_url_field.allow_tags = True
  my_url_field.short_description = 'Generate Report'
  
  

admin.site.register(Patient)
admin.site.register(Test,TestAdmin)
admin.site.register(TestScore)

admin.site.register(Physician)
admin.site.register(SpeechEvaluationReport,SpeechEvaluationReportAdmin)
