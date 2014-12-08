__author__ = 'cltanuki'
from rest_framework import viewsets
from . import models, serializers


class ReportViewset(viewsets.ModelViewSet):

    serializer_class = serializers.ReportSerializer
    queryset = models.Report.objects.all()