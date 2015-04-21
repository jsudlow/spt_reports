from django.shortcuts import render
from reports.models import SpeechEvaluationReport,Patient
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import inch
from reportlab.lib.units import cm
from django.template.loader import get_template
from django.template import Context
from xhtml2pdf import pisa 
# Create your views here.
def index(request):
    return render(request, 'reports/index.html')
def generate_speech_eval_report2(request, report_id):
    #response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="speech_evaluation_report.pdf"'
    
    report = SpeechEvaluationReport.objects.get(id=report_id)
    patient = Patient.objects.get(id=report.patient_id)
    #logo = ImageReader('http://localhost:8000/static/logo_pdf.png')
    context = {'report': report, 'patient': patient}
    return render(request, 'reports/generate_speech_eval_report.html',context)
   # p = canvas.Canvas(response,pagesize=letter)
   # width, height = letter
   # p.drawString(100, 100, "Hello world.")
   # p.drawImage(logo,10,9*inch,width=None,height=None)

    # Close the PDF object cleanly, and we're done.
    #p.showPage()
    #p.save()
    #return response

def generate_speech_eval_report(request, report_id):
    
    report = SpeechEvaluationReport.objects.get(id=report_id)
    patient = Patient.objects.get(id=report.patient_id)
    data = {'report': report, 'patient': patient}
    template = get_template('reports/generate_speech_eval_report.html')
    html  = template.render(Context(data))
    print html

    file = open('test.pdf', "w+b")
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,
            encoding='utf-8')


    file.seek(0)
    pdf = file.read()
    
    file.close()            
    return HttpResponse(pdf,content_type='application/pdf')


    