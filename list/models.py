from django.db import models


# Create your models here.
class CompanyOwner(models.Model):
    class Meta(object):
        verbose_name = 'Owner'
        verbose_name_plural = 'Owners'

    owner_name = models.CharField(max_length=30, null=True, blank=True)
    owner_surname = models.CharField(max_length=30, null=True, blank=True)
    owner_email = models.EmailField(null=True, blank=True)
    owner_company = models.ForeignKey('Company')

    def __str__(self):
        return '%s %s' % (self.owner_name, self.owner_surname)


class Company(models.Model):
    class Meta(object):
        verbose_name = 'Company'
        verbose_name_plural = 'Companys'

    company_name = models.CharField(max_length=128, null=True, blank=True)
    state = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=128, null=True, blank=True)
    street = models.CharField(max_length=128, null=True, blank=True)
    zip = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return '%s' % self.company_name