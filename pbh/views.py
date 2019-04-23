from django.shortcuts import render,HttpResponse
from  pbh.forms import HomeForm
from django.views.generic import TemplateView
from pbh.models import UserProfile
from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

def home(request):
	username = None
	if request.user.is_authenticated:
		username = request.user.get_username()
	return render(request,'pbh/main.html', {'username': username})

def about(request):
	username = None
	if request.user.is_authenticated:
		username = request.user.get_username()
	return render(request,'pbh/ABOUT.html', {'username': username})

def contact(request):
	username = None
	if request.user.is_authenticated:
		username = request.user.get_username()
	return render(request,'pbh/contact.html', {'username': username})

def fees(request):
	username = None
	if request.user.is_authenticated:
		username = request.user.get_username()
	return render(request,'pbh/FEE.html', {'username': username})

def rules(request):
	username = None
	if request.user.is_authenticated:
		username = request.user.get_username()
	return render(request,'pbh/RULES.html', {'username': username})

def view_details(request):
	username = None
	if request.user.is_authenticated:
		username = request.user.get_username()
	else:
		return redirect('/pbh/login/')
	post = None
	try:
		post=UserProfile.objects.get(user=request.user)
	except:
		## no details found
		pass

	return render(request,'pbh/view_details.html',{'post':post, 'username': username})

def edit_details(request):
	if not request.user.is_authenticated:
		return redirect('/pbh/login/')
	username = request.user.get_username()
	if(request.method=='POST'):
		try:
			user_details = UserProfile.objects.get(user=request.user)
			form=HomeForm(request.POST, user=request.user, instance=user_details)
		except:
			form=HomeForm(request.POST, user=request.user)
		if(form.is_valid()):
			form.save()
	else:
		try:
			user_details = UserProfile.objects.get(user=request.user)
			if user_details is not None:
				form=HomeForm(initial={
					'srn': user_details.srn,
					'name': user_details.name,
					'father_name': user_details.father_name,
					'mothers_name': user_details.mothers_name,
					'age': user_details.age,
					'dob': user_details.dob,
					'email': user_details.email,
					'pno': user_details.pno,
					'ppno': user_details.ppno,
					'field': user_details.field,
					'address': user_details.address,
					'lg_name': user_details.lg_name,
					'lg_age': user_details.lg_age,
					'lg_dob': user_details.lg_dob,
					'lg_pno': user_details.lg_pno,
					'lg_address': user_details.lg_address,
					}, user=request.user)
		except:
			form = HomeForm(user=request.user)
	return render(request,'pbh/edit_details.html', {'form': form, 'username': username})

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('/pbh')
	else:
		form = UserCreationForm()
	return render(request, 'pbh/Register.html', {'form': form})