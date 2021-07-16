from django.db import models
from django.contrib.auth.models import User

class Labadmin(models.Model):

    user =models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    labname= models.CharField(max_length=100,null=True)
    adminemail = models.CharField(max_length=100,null=False)
    adminpssword = models.CharField(max_length=100,null=False)
    labaddress = models.CharField(max_length=100,null=True)
    lablocation = models.CharField(max_length=500,null=True)
    labtests = models.CharField(max_length=100, null=True)
    gst = models.IntegerField(null=True)
    is_admin = models.BooleanField(null=True)
    file = models.FileField(upload_to="documents", null=True)

    class Meta:
        verbose_name_plural ="labupdates"
    def __str__(self):
        return self.labname

