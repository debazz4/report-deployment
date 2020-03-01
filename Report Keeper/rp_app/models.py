from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q

class RecordQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (
                Q(cr_no__icontains=query) |
                Q(cer_no__icontains=query) |
                Q(complaint_name__icontains=query) |
                Q(suspect_name__icontains=query)
            )
            qs = qs.filter(or_lookup).distinct() # distinct is often necessary with Q 
        return qs

class RecordManager(models.Manager):
    def get_queryset(self):
        return RecordQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)

class CreateRecord(models.Model):
    
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cr_no = models.CharField(max_length=20)
    cer_no = models.CharField(max_length=20, blank=True, null=True)
    date_recieved = models.CharField(max_length=20)
    date_assigned = models.CharField(max_length=20)
    complaint_name = models.CharField(max_length=50)
    complaint_address = models.CharField(max_length=100, blank=True, null=True)
    complaint_state_of_origin = models.CharField(max_length=20, blank=True, null=True)
    complaint_LGA = models.CharField(max_length=20, blank=True, null=True)
    complaint_sex = models.CharField(max_length=6, choices=SEX_CHOICES )
    complaint_age = models.IntegerField(blank=True, null=True)
    suspect_name = models.CharField(max_length=50)
    suspect_address = models.CharField(max_length=100, blank=True, null=True)
    suspect_state_of_origin = models.CharField(max_length=20, blank=True, null=True)
    suspect_LGA = models.CharField(max_length=20, blank=True, null=True)
    suspect_sex = models.CharField(max_length=6, choices=SEX_CHOICES )
    suspect_age = models.IntegerField(blank=True, null=True)
    offence = models.CharField(max_length=100)
    amount_involved_naira = models.IntegerField(blank=True, null=True)
    amount_involved_dollar = models.IntegerField(blank=True, null=True)
    cfa_involved = models.CharField(max_length=20, blank=True, null=True)
    others_involved = models.CharField(max_length=20, blank=True, null=True)
    amount_recieved_naira = models.IntegerField(blank=True, null=True)
    amount_recieved_dollar = models.IntegerField(blank=True, null=True)
    cfa_recieved = models.CharField(max_length=20, blank=True, null=True)
    others_recieved = models.CharField(max_length=20, blank=True, null=True)
    team = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    date_sent_to_legal = models.CharField(max_length=20, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True) 

    objects = RecordManager()


    def __str__(self):
        return self.cr_no