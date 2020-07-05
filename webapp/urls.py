from django.conf.urls import url
from django.urls import include, path
from webapp import views
urlpatterns = [
 path(r'^$', views.index, name='index'),
 path('patient-registrations-landing/', views.patient_registrations_landing, name='patient_registrations_landing'),
 path('patient-registrations/', views.patient_registrations, name='patient_registrations'),
 path('patient-deatils/', views.patient_details, name='patient_details')

]