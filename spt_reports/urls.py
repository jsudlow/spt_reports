from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'spt_reports.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^reports/', include('reports.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^$', 'reports.views.index', name='index')
]
