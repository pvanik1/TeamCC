from django.shortcuts import render
from django.http import HttpResponse
from fixit.forms import UserForm, IssueForm

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# register, login and logout stuff

def login(request):

	# If the user is logged in, go to Index (homepage)
	if request.user.is_authenticated:
		return render(request, 'fixit/index.html')

	# Otherwise display login.html, which shows the login and register forms
	else:
		registered = False
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user_form = UserForm(data=request.POST)

			if (username != '') and (password != ''):
				user = authenticate(username=username, password=password)

				if user:
					if user.is_active:
						login(request, user)
						return HttpResponseRedirect(reverse('login'))
					else:
						context_dict = {'infoMessage': "Your login has expired. Please " + '<a href="{% url userInactive %} ">login again.</a>'}
						return render(request, 'fixit/userInactive.html', context = context_dict)
				else:
					print("Invalid login details: {0}, {1}".format(username, password))
					context_dict = {'infoMessage': "Your login details do not match. Please try again."}
					return render(request, 'fixit/invalidLogin.html', context = context_dict)

			if (user_form.is_valid()):
				user = user_form.save()
				user.set_password(user.password)
				user.save()
				registered = True

			else:
				print (user_form.errors)

		else:
			user_form = UserForm()
			return render(request, 'fixit/login.html', 
					{'user_form': user_form, 
					'registered': registered})

def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('login'))

def index(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'fixit/about.html')



