from django.shortcuts import render

# Create your views here.
def frontpage_v(request):
  return render(request, 'core/frontpage.html')