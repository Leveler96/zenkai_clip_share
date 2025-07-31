from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm


# Create views here.
@login_required  # decorator that ensures that logged-in users can access this view
def dashboard(request):
    # user object is available in the template automatically if users can access this view
    return render(request, 'users/dashboard.html')


def register(request):
    if request.method == 'POST':
        # if the request is a POST, it means the form has been submitted
        form = UserRegistrationForm(request.POST)  # populate form with submitted data
        if form.is_valid():
            form.save()  # save the new user to the database
            username = form.cleaned_data.get('username')
            # could potentially add an account creation  success messege here

            return redirect('login')  # redirect to the login page after successful login
    else:
        # if request is a GET then I need to display an empty form
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})
