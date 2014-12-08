from django.db import models
from django.utils.translation import ugettext as _
from erp.enterprise.models import CorpObject
from erp.directory.models import Person


class Report(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField()
    reporter = models.ForeignKey(Person)
    file = models.FileField()
    begins = models.DateField(verbose_name=_('Begins at'))
    ends = models.DateField(verbose_name=_('Ends at'))
    section = models.ForeignKey('Section', related_name='reports')
    index = models.SmallIntegerField()


class Section(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField()
    master = models.ForeignKey(Person)
    begins = models.DateField(verbose_name=_('Begins at'))
    ends = models.DateField(verbose_name=_('Ends at'))
    conf = models.ForeignKey('Conference', related_name='shedule')
    index = models.SmallIntegerField()


class Conference(models.Model):
    begins = models.DateField(verbose_name=_('Begins at'))
    ends = models.DateField(verbose_name=_('Ends at'))
    place = models.ForeignKey(CorpObject, verbose_name=_('Place'))
    orgs = models.ManyToManyField(Person, verbose_name=_('Managers'))
    thesis_rules = models.TextField(verbose_name=_('Thesis Rules'))

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('prj_item', args=[str(self.slug)])