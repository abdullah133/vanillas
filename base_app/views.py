from django.shortcuts import render
from django.views.generic.base import TemplateView




class HomeView(TemplateView):
    template_name = 'base_app/base.html'


    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['auf_welcher_seite'] = 'home'
        return context

class UnterschreibnView(TemplateView):
    template_name = 'base_app/unterschreiben.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        return context
