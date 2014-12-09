__author__ = 'cltanuki'
from . import models
from erp.planning.models import Project
from rest_framework import serializers


class ReportSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Report
        fields = ('title', 'slug', 'reporter', 'file', 'begins', 'ends', 'index')


class SectionSerializer(serializers.HyperlinkedModelSerializer):
    reports = ReportSerializer(many=True)

    class Meta:
        model = models.Section
        fields = ('title', 'slug', 'master', 'begins', 'ends', 'index', 'reports')


class ConfDataSerializer(serializers.HyperlinkedModelSerializer):
    schedule = SectionSerializer(many=True)
    place = serializers.HyperlinkedIdentityField(view_name='obj-detail')

    class Meta:
        model = models.Conference
        fields = ('begins', 'ends', 'place', 'orgs', 'thesis_rules', 'schedule')


class ConfSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project