from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from databutler.models import get_programs, get_friends


class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['programs'] = get_programs()
        context['friends'] = get_friends()

        return context
