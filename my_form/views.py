from django.shortcuts import render,redirect
from .models import Clients,ClientDetail
from django.views.generic import CreateView, TemplateView
from .forms import ClientCreateForm, AddClientForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

def home(request):  #home view
   return render(request, 'my_form/home.html', {'clients': Clients.objects.all()})

# Adding client
def addclient(request):  # Here we add our clients
    if request.method == 'POST':
        form = AddClientForm(request.POST)
        if form.is_valid():
            form.save()
            First_name = form.cleaned_data.get('First_name')
            return redirect('home-page')
    else:
        form = AddClientForm()
    return render(request, 'my_form/client.html', {'form': form})

# Client details view

def client_details(request,pk):
    try:
        
        data = ClientDetail.objects.get(id = pk)   #Stores the data based on user request
        context = {                                #Captures exceptions and sends message
            'detail':data
        }
        return render(request, 'my_form/detail.html', context)
    except ClientDetail.DoesNotExist:
        messages.warning(request, 'Please fill the client details')
        return redirect('home-page')
        
#  saving the client info from online form

def createclient(request):
    if request.method == 'POST':
        form = ClientCreateForm(request.POST)
        if form.is_valid():
            form.save()
            fullname = form.cleaned_data.get('fullname')
            email = form.cleaned_data.get('email')
            web_address = form.cleaned_data.get('web_address')
            return redirect('home-page')
    else:
        form = ClientCreateForm()
    return render(request, 'my_form/create.html', {'form': form})


