__author__ = 'cltanuki'
from rest_framework import viewsets
from . import models, serializers
from erp.planning.models import Project


class ReportViewset(viewsets.ModelViewSet):

    serializer_class = serializers.ReportSerializer
    queryset = models.Report.objects.all()


class SectionViewSet(viewsets.ModelViewSet):

    serializer_class = serializers.SectionSerializer
    queryset = models.Section.objects.all()


class ConfViewset(viewsets.ModelViewSet):

    serializer_class = serializers.ConfSerializer
    queryset = Project.objects.filter(item_type_id=22)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = serializers.ConfDataSerializer
        self.queryset = models.Conference.objects.all()
        return super(ConfViewset, self).retrieve(request, *args, **kwargs)