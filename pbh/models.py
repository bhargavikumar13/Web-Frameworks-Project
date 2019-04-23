from django.db import models
from django.contrib.auth.models import User
import datetime

class UserProfile(models.Model):
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		primary_key=True)
	srn=models.CharField(max_length=13,default='')
	name=models.CharField(max_length=100)
	father_name=models.CharField(max_length=100)
	mothers_name=models.CharField(max_length=100)
	age=models.IntegerField()
	dob = models.DateField(("Date"), default=datetime.date.today)
	email=models.EmailField(default='')
	pno=models.IntegerField(default=0)
	ppno=models.IntegerField(default=0)
	CSE = 'CSE'
	ECE = 'ECE'
	EEE = 'EEE'
	ME = 'ME'
	CHOICES = (
		(CSE, 'CSE'),
		(ECE, 'ECE'),
		(EEE, 'EEE'),
		(ME, 'ME'),
		)
	field = models.CharField(max_length=3,
                                      choices=CHOICES,
                                      default=CSE)
	address=models.TextField()
	lg_name=models.CharField(max_length=100)
	lg_age=models.IntegerField(default=0)
	lg_dob= models.DateField(("Date"), default=datetime.date.today)
	lg_pno=models.IntegerField(default=0)
	lg_address=models.TextField()
