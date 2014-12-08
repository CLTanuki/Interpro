__author__ = 'cltanuki'
from . import models
from erp.planning.models import Project
from rest_framework import serializers


class ReportSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Conference
        fields = ('title', 'slug', 'reporter', 'file', 'begins', 'ends', 'index')