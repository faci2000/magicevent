from .views import EventsListView,EventList
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path,include

urlpatterns = [
    path('',EventsListView.as_view(),name='events/events_list.html'),
    path('sign/<int:pk>/',EventsListView.as_view(),name='events/events_list.html'),
    path('api/',EventList.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)