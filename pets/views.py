from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.utils import timezone
from django.http import HttpResponse 
from pets.models import Pet, Appointment
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.

class HomePage(ListView):

    def get(self, request):
        return render(request, 'home.html')
        
            
class PetListView(ListView):
    
    model = Pet
    
    def get(self, request):
        pets = self.get_queryset().all()
        return render(request, 'pet/PetsList.html', {'pets': pets})

class PetCreateView(CreateView):

    model = Pet

    fields = ['owner', 'pet_name', 'species', 'breed', 'weight_in_pounds']
    template_name = 'pet/CreatePet.html'

class PetDetailView(DetailView):

    def get(self, request, pet_id):
        return render(request, 'pet/PetDetail.html', {'pet': Pet.objects.get(id=pet_id)})

class AppointmentCreation(CreateView):

    model = Appointment

    fields = ['date_of_appointment', 'duration_minutes', 'special_instructions', 'pet']
    template_name = 'schedule/CreateAppointment.html'

class CalendarView(ListView):

    model = Appointment

    def get(self, request):
        appointments = self.get_queryset().all()
        return render(request, 'schedule/AppointmentList.html', {'appointments': appointments.filter(
            date_of_appointment__gte=timezone.now()
        ).order_by('date_of_appointment', 'duration_minutes')})
