from django.db import models  
class login(models.Model): 
	Username=models.CharField(max_length=50)
	password=models.CharField(max_length=50)

class registration(models.Model):
	Username=models.CharField(max_length=50)
	password=models.CharField(max_length=50)
	emailid=models.CharField(max_length=50)
	Phoneno=models.IntegerField()

class contact(models.Model):
	FirstName=models.CharField(max_length=50)
	LastName=models.CharField(max_length=50)
	emailid=models.CharField(max_length=50)
	Phoneno=models.IntegerField()


class Meta:
	db_table = "login"
class Meta:
	db_table="registration"

class Meta:
	db_table="contact"









# Create your models here.
