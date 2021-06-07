from django.db import models

class User_info(models.Model):
    Address=models.CharField(max_length=100)
    Businessname=models.CharField(max_length=100)
    Person_name=models.CharField(max_length=100)
    contact=models.IntegerField()
    verifiedstatus=models.CharField(max_length=1)
    timestamp=models.DateTimeField(auto_now=True)

