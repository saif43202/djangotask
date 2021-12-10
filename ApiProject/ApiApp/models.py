from django.db import models

class User(models.Model):
	username=models.CharField(max_length=50)
	firstname=models.CharField(max_length=50)
	lastname=models.CharField(max_length=50)
	emailid=models.CharField(max_length=50)
	password=models.CharField(max_length=50)
	class Meta:
		db_table='User' 

	def __str__(self):
		return self.username	
# Create your models here.
