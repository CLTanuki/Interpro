from django.shortcuts import render
from erp.planning.models import Project
from django.views.generic import DetailView, View, ListView, TemplateView
import logging
logger = logging.getLogger(__name__)


class ConfIndex(TemplateView):

    template_name = 'conf/index.html'


class ConfMain(DetailView):
    model = Project
    # template_name = 'conf/index.html'

    def get_context_data(self, **kwargs):
        context = super(ConfMain, self).get_context_data(**kwargs)
        context['confs'] = Project.objects.filter(item_type_id=17).values()#  .filter(status=1)
        return context


