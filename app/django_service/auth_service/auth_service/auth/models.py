from django.db import models

class Auth(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=255)
    user_id = models.IntegerField()

