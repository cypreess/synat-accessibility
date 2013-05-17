# Create your views here.
from django.views.generic import TemplateView
from synat_help.help_example.models import Category, Article

class ProsteView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(ProsteView, self).get_context_data(**kwargs)
        context['mode'] = 'proste'
        context['categories'] = [] #Category.objects.all
        return context

class ZaawansowaneView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(ZaawansowaneView, self).get_context_data(**kwargs)
        context['mode'] = 'zaawansowane'
        context['categories'] = Category.objects.all
        return context

class WiecejView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(WiecejView, self).get_context_data(**kwargs)
        context['article'] = Article.objects.get(id=kwargs['identifier'])
        context['categories'] = Category.objects.all
        return context
