from .views import EventsListView,EventList,conf#,ClientEvents
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path,include

urlpatterns = [
    path('',EventsListView.as_view(),name='events/events_list.html'),
    path('confirm/<int:pk>',conf,name='events/confirm.html'),
    path('<int:pk>/',EventsListView.as_view(),name='events/events_list.html'),
    #path('add/',ClientEvents.as_view()),
    path('api/',EventList.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)