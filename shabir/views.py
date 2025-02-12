# Create your views here.
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
import json, requests
# Create your views here.
with open('portfolio.config.json', 'r') as fp:
	config = json.load(fp)
def index(request):
	projects = Projects.objects.all()
	ctx = {'config': config['Config'],'projects': projects if projects else None}
	if request.method == "POST":
		email = request.POST.get('email')
		name = request.POST.get('name')
		message = request.POST.get('message')
		data = {
		"content" : f"**EMAIL**: {email}\n**NAME:** {name}\n**MESSAGE:** {message}"
		}
		result = requests.post(config['Config']["contact"]["webhook_url"], json=data)
	return render(request, 'pages/base.html',ctx)

def blog(request):
	return HttpResponse("Coming soon.")

def mobile_view(request):
      return render(request, 'pages/mobile.html')

def desktop_view(request):
      return render(request, 'pages/index.html')




def project(request):
    projects = Projects.objects.all()
    context = {
        'projects': projects,
        'config': {
            'name': 'Shabir',
            'country': 'India',
        }
    }
    return render(request, 'pages/project.html', context)

# views.py


from django.shortcuts import render, redirect
from .models import Contact

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        company = request.POST.get('company')
        designation = request.POST.get('designation')
        message = request.POST.get('message')

        # Save the form data into the Contact model
        contact = Contact(name=name, email=email, company=company, designation=designation, message=message)
        contact.save()

        # Redirect to a thank you page after the form is successfully submitted
        return redirect('thank_you')

    return render(request, 'pages/contact.html')



def thank_you(request):
      return render(request, 'pages/thank_you.html')

from django.http import FileResponse
from django.conf import settings
import os

def download_resume(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'files/shabeer.pdf')
    return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='shabeer.pdf')
