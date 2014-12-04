from django.db import models
from django.utils.translation import ugettext as _
from erp.enterprise.models import CorpUser, CorpObject
from erp.directory.models import Person


class Conference(models.Model):
    begins = models.DateField(verbose_name=_('Begins at'))
    ends = models.DateField(verbose_name=_('Ends at'))
    place = models.ForeignKey(CorpObject, verbose_name=_('Place'))
    orgs = models.ManyToManyField(Person, verbose_name=_('Managers'))
    schedule = models.TextField(verbose_name=_('Shedule'))
    thesis_rules = models.TextField(verbose_name=_('Thesis Rules'))

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('prj_item', args=[str(self.slug)])


class ConfMember(models.Model):
    user = models.ForeignKey(Person)
    is_reporter = models.BooleanField(verbose_name=_('Reporter'), default=False)
    conf = models.ForeignKey(Conference)

# class Reports(models.Model):
#     pass