__author__ = 'cltanuki'
from . import models
from erp.planning.models import Project
from rest_framework import serializers


class GoodsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Conference
        fields = ('begins', 'ends', 'cat', 'rel_cat', 'desc', 'pic')