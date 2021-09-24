from django.db import models
from user_login.models import UserDetails
# Create your models here.
class Tag(models.Model):
    pk_bint_id = models.BigAutoField(primary_key=True)
    vchr_title = models.CharField(max_length=100, blank=True, null=False ,unique=True)

class Snippet(models.Model):
    pk_bint_id = models.BigAutoField(primary_key=True)
    fk_tag = models.ForeignKey(Tag, models.DO_NOTHING, blank=True, null=True)
    vchr_content = models.TextField(blank=True, null=True)
    fk_created_by = models.ForeignKey(UserDetails, models.DO_NOTHING, blank=True, null=True)
    dat_created = models.DateTimeField(blank=True, null=True)
