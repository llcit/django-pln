from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

from autoslug import AutoSlugField
from filer.fields.image import FilerImageField

class AppType(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class AppFormat(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class AppFunction(models.Model):
    name = models.CharField(max_length=254)


    def __str__(self):
        return self.name

class AppPrice(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class AppSupport(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class App(models.Model):
    class Meta:
        app_label = 'pln'
        ordering = ["id"]

    Bool = (
        (True, 'Yes'),
        (False, 'No'),
    )
    name = models.CharField(max_length=254, blank=False, default='', unique=True)
    slug = AutoSlugField(populate_from='name')
    description = models.TextField(null=True, blank=True)
    icon = models.URLField(max_length=254, null=True, blank=True)
    icon_image = FilerImageField(blank=True, null=True, on_delete=models.SET_NULL)
    privacy = models.CharField(max_length=254, null=True, blank=True)
    tutorial = models.CharField(max_length=254, null=True, blank=True)
    url = models.CharField(max_length=254, null=True, blank=True)
    testimonial = models.CharField(max_length=255, null=True, blank=True)
    type = models.ManyToManyField(AppType)
    format = models.ManyToManyField(AppFormat)
    function = models.ManyToManyField(AppFunction)
    price = models.ManyToManyField(AppPrice)
    support = models.ManyToManyField(AppSupport)
    is_avaiable = models.BooleanField(choices=Bool, default=True)

    def get_absolute_url(self):
        return reverse('pln:pln_detail', kwargs={'slug': self.slug, })

    def __str__(self):
        return self.name
