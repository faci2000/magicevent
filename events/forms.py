from .models import Client,Event
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import re 

def check(email):  
    if(re.search(regex,email)):  
        return True      
    False

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields =['title','start_date','end_date','thumbnail',]


class ClientForm(ModelForm):
    events = EventForm()
    class Meta:
        model = Client
        fields =['name','surname','mail','events',]

    def clean_renewal_date(self):
        mail = self.cleaned_data['mail']
        if check(regex,mail):
            raise ValidationError(_('Invalid email'))
        return mail