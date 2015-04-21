from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^generate_speech_eval_report/(?P<report_id>[0-9]+)/$', views.generate_speech_eval_report, name='generate_speech_eval_report'),
]
