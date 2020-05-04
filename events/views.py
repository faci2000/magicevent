from django.shortcuts import render

from .models import Event
from .serializers import EventSerializer,ClientSerializer
from .forms import ClientForm

from django.shortcuts import render 
from django.views.generic.list import ListView
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



class EventsListView(APIView):
    def get(self,request,*args, **kwargs):
        template_name='events/events_list.html'
        context ={ 'events':Event.objects.all()}
        return render(request,template_name,context)
    def post(self,request, pk=None, *args, **kwargs):
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
        context ={'form':form, 'events':Event.objects.all() }
        return render(request,'events/events_list.html',context)


class EventList(APIView):
    def get(self, request, format=None):
        questions = Event.objects.all()
        serializer = EventSerializer(questions, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventDetail(APIView):
    def delete(self, request, pk, format=None):
        Question = self.get_object(pk)
        if(Question.end_date-Question.start_date)>=2:
            Question.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=staticmethod.status.HTTP_400_BAD_REQUEST)

