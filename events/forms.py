from .models import Client,Event
from django.forms import ModelForm

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields =['title','start_date','end_date','thumbnail',]


class ClientForm(ModelForm):
    events = EventForm()
    class Meta:
        model = Client
        fields =['name','surname','mail','events',]