from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create views here.
@login_required  # decorator that ensures that logged in users can access this view
def dashboard(request):
    # user object is available in the template automatically if users can access this view
    return render(request, 'users/dashboard.html')
