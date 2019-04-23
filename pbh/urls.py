from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns=[
	path('login/', LoginView.as_view(template_name='pbh/login.html'), name="login"),
	path('logout/', LogoutView.as_view(template_name='pbh/logout.html'), name="logout"),
	path('',views.home,name='home'),
	path('about/',views.about,name='about'),
	path('contact/',views.contact,name='contact'),
	path('view_details/',views.view_details,name='view_details'),
	path('edit_details/',views.edit_details,name='edit_details'),
	path('pbh/fees/', views.fees,name='fees'),
	path('pbh/rules/', views.rules,name='rules'),
	path('pbh/register/', views.register, name='register'),

]