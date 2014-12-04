from django.db import models
from django.utils.translation import ugettext as _
from erp.enterprise.models import CorpObject
from erp.directory.models import Person


class Reports(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField()
    reporter = models.ForeignKey(Person)
    file = models.FileField()
    begins = models.DateField(verbose_name=_('Begins at'))
    ends = models.DateField(verbose_name=_('Ends at'))


class Section(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField()
    reports = models.ForeignKey(Reports)
    begins = models.DateField(verbose_name=_('Begins at'))
    ends = models.DateField(verbose_name=_('Ends at'))


class Conference(models.Model):
    begins = models.DateField(verbose_name=_('Begins at'))
    ends = models.DateField(verbose_name=_('Ends at'))
    place = models.ForeignKey(CorpObject, verbose_name=_('Place'))
    orgs = models.ManyToManyField(Person, verbose_name=_('Managers'))
    schedule = models.TextField(verbose_name=_('Shedule'))
    thesis_rules = models.TextField(verbose_name=_('Thesis Rules'))
    sections = models.ForeignKey(Section)

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('prj_item', args=[str(self.slug)])