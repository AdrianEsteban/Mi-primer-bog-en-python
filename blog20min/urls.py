from django.conf.urls import patterns, include, url
from blog.views import IndexView , Entrada
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog20min.views.home', name='home'),
    # url(r'^blog20min/', include('blog20min.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),    
    url(r'^markdown/', include('django_markdown.urls')),
    url(r'^$', IndexView.as_view()),
    url(r'^entrada/(?P<slug>[-\w]+)', Entrada.as_view()),
)