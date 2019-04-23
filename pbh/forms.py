from django import forms
from .models import UserProfile
from django.contrib.auth.models import User

class HomeForm(forms.ModelForm):
	srn=forms.CharField(max_length=13) 
	name=forms.CharField(max_length=100)
	father_name=forms.CharField(max_length=100)
	mothers_name=forms.CharField(max_length=100)
	age=forms.IntegerField()
	dob = forms.DateField()
	email=forms.EmailField()
	pno=forms.IntegerField()
	ppno=forms.IntegerField()
	CHOICES = (('CSE', 'CSE'),('ECE', 'ECE'),('ME','ME'),('EEE','EEE'))
	field = forms.ChoiceField(choices=CHOICES)
	address=forms.Textarea()
	lg_name=forms.CharField(max_length=100)
	lg_age=forms.IntegerField()
	lg_dob= forms.DateField()
	lg_pno=forms.IntegerField()
	lg_address=forms.Textarea()
        
	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user','')
		super(HomeForm, self).__init__(*args, **kwargs)
		self.fields['user']=forms.ModelChoiceField(queryset=User.objects.filter(username=user.get_username()))

	class Meta:
		model= UserProfile
		fields='__all__'
