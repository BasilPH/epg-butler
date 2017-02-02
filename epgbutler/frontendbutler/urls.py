# urls.py
from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^epg$', TemplateView.as_view(template_name='dashboard.html')),
]
