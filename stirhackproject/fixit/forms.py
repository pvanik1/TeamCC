from django import forms
from fixit.models import UserProfile, Issue
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		
class IssueForm(forms.ModelForm):
	issueID = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
	# TODO how to make ID automatically increment with each added ID?
	title = forms.CharField(max_length = 128, help_text = "What issue would you like to report?", required = True)
	description = forms.CharField(max_length = 255, help_text = "Please provide details of the issue", required = True)
	location_bdg = forms.CharField(max_length = 128, help_text = "In which building is the issue?", required = True)
	location_detail = forms.CharField(max_length = 128, help_text = "Please provide details of the room or space.", required = True)
	upvotes = forms.IntegerField(widget = forms.HiddenInput(), initial = 0)
	# TODO image upload
	# TODO input different tags to store them in a 'tags' list of the Issue model
	
	# An inline class to provide additional information on the form.
	class Meta:
		# Provide an association between the ModelForm and a model
		model = Issue 
		exclude = ('issueID','upvotes')
		# What was the following line for in rango? 
		# fields = ('name',)