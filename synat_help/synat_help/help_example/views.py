# Create your views here.
from django.views.generic import TemplateView

class ProsteView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(ProsteView, self).get_context_data(**kwargs)
        context['mode'] = 'proste'
        return context

class ZaawansowaneView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(ZaawansowaneView, self).get_context_data(**kwargs)
        context['mode'] = 'zaawansowane'
        return context
