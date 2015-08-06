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

def link_callback(uri, rel):
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, ""))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                    'media URI must start with %s or %s' % \
                    (sUrl, mUrl))
    return path

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

    dob = patient.date_of_birth
    date_of_visit = report.date_of_visit
    years = (date_of_visit - dob).days/365
    print "dob", dob
    print "visit date",date_of_visit

    print "years:", years


    data = {'report': report, 'patient': patient, 'years': years}
    template = get_template('reports/generate_speech_eval_report.html')
    html  = template.render(Context(data))
    #print html
    print 'about to try and open file'
    file = open('C:/test.pdf', "w+b")
    print 'opend file'
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,
            encoding='utf-8')

    print 'created pdf'
    file.seek(0)
    pdf = file.read()
    
    file.close()            
    return HttpResponse(pdf,content_type='application/pdf')


    