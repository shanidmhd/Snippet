from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserDetails(User,models.Model):
    vchr_name = models.CharField(max_length=100, blank=True, null=True)
    dat_dob = models.DateField(blank=True, null=True)
    bint_phone = models.BigIntegerField(blank=True, null=True)

class SessionHandler(models.Model):
    pk_bint_id = models.BigAutoField(primary_key=True)
    fk_user = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True,related_name ='sessionhandler')
    vchr_session_key = models.CharField(max_length=500, blank=True, null=True)
