from django.contrib.auth import login, logout
from django.conf import settings
from django.shortcuts import render, redirect

from .forms import SignUpForm

# Create your views here.
def frontpage_v(request):
  return render(request, 'core/frontpage.html')

def logout_v(request):
  logout(request)
  return redirect(settings.LOGOUT_REDIRECT_URL)

def signup_v(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    
    if form.is_valid():
      user = form.save()
      
      login(request, user)
      
      return redirect('frontpage')
  else:
    form = SignUpForm()
  
  return render(request, 'core/signup.html', {'form':form})