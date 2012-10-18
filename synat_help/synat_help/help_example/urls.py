from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from synat_help.help_example.views import ProsteView, ZaawansowaneView

urlpatterns = patterns('',
        url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
        url(r'^proste/$', ProsteView.as_view(template_name='proste.html'), name='proste'),
        url(r'^proste/wiecej/$', ProsteView.as_view(template_name='wyszukiwanie_proste_wiecej.html'), name='proste_wiecej'),

        url(r'^zaawansowane/$', ZaawansowaneView.as_view(template_name='zaaw.html'), name='zaawansowane'),
        url(r'^zaawansowane/wiecej/$', ZaawansowaneView.as_view(template_name='wyszukiwanie_zaaw_wiecej.html'), name='zaawansowane_wiecej'),


        url(r'^slowa_kluczowe/wiecej/$', TemplateView.as_view(template_name='slowa_kluczowe_wiecej.html'), name='slowa_kluczowe_wiecej'),
        url(r'^tytul/wiecej/$', TemplateView.as_view(template_name='tytul_wiecej.html'), name='tytul_wiecej'),
        url(r'^autor/wiecej/$', TemplateView.as_view(template_name='autor_wiecej.html'), name='autor_wiecej'),
        url(r'^temat/wiecej/$', TemplateView.as_view(template_name='temat_wiecej.html'), name='temat_wiecej'),
        url(r'^nazwa/wiecej/$', TemplateView.as_view(template_name='nazwa_wiecej.html'), name='nazwa_wiecej'),
        url(r'^seria/wiecej/$', TemplateView.as_view(template_name='seria_wiecej.html'), name='seria_wiecej'),
)

