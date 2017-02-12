from django.shortcuts import render
from django.http import HttpResponse

from fixit.models import Issue
from fixit.forms import UserForm, IssueForm

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# register, login and logout stuff

def register(request):
    # A boolean value for telling the template whether the registration
    # was successful. Set to False initially. Code changes value
    # to True when registration succeeds.
    registered = False
    # If it's a HTTP POST, we're interested in processing
    # from data.
    if request.method=='POST':
        #Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data = request.POST)
        # If the forms is valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to indicate that the template
            # registration was successful.
            registered = True
        else:
            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            print(user_form.errors)
    else:
        # Not a HTTP POST, so we render our form using two ModelForm instances.
        # These forms will be blank, ready for user input.
        user_form = UserForm()

    # Render the template depending on the context.
    return render(request,
                  'fixit/register.html',
                  {'user_form': user_form,
                   'registered': registered})

def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
    # Gather the username and password provided by the user.
    # This information is obtained from the login form.
    # We use request.POST.get('') as opposed
    # to request.POST[''], because the 
    # request.POST.get('') returns None if the 
    # value does not exist, while request.POST[''] 
    # will raise a KeyError exception. 
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'fixit/login.html', {})

def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('login'))

def index(request):
    issue_list = Issue.objects.order_by('id')
    context_dict = {'issues': issue_list}
    return render(request, 'fixit/index.html', context=context_dict)

def about(request):
	return render(request, 'fixit/about.html')

def addIssue(request):
    
    if request.method == 'POST':
        issue_form = IssueForm(request.POST, request.FILES)
        if issue_form.is_valid():
            issue = issue_form.save(commit=False)
            issue.save()
        else:
            print(issue_form.errors)

    issue_form = IssueForm()

    return render(request, 'fixit/addIssue.html', {'issue_form':issue_form})



