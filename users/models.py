from django.db import models

class Users(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  class Meta:
        db_table = 'users'  # Your custom table name
