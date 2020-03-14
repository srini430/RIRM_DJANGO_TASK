from django.forms import ModelForm
from .models import ClientDetail,Clients

class AddClientForm(ModelForm):
    class Meta:
        model = Clients
        fields = ['First_name']

class ClientCreateForm(ModelForm):
    class Meta:
        model = ClientDetail
        fields = '__all__'

    
