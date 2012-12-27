from django.db import models
from django.utils.translation import ugettext_lazy as _


class State(models.Model):
    name = models.CharField(max_length=250)
    abbreviation = models.CharField(max_length=10)

    class Meta:
        verbose_name = _(u'State')
        verbose_name_plural = _(u'States')

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=250)
    state = models.ForeignKey(State, related_name='cities')

    class Meta:
        verbose_name = _(u'City')
        verbose_name_plural = _(u'Cities')

    def __unicode__(self):
        return u'%s, %s' % (self.name, self.state)
