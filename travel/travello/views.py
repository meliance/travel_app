from django.shortcuts import render
from .models import Destination
from .models import Trip
# Create your views here.
def index(request):

  dests = Destination.objects.all()
  return render(request, 'index.html', {'dests': dests} )

def search_trip(request):
    if request.method == 'GET':
        city = request.GET.get('city', '')
        departure = request.GET.get('departure', '')
        # arrival = request.GET.get('arrival', '')
        # budget = request.GET.get('budget', '')

        # Check if the city exists in the database
        if Trip.objects.filter(city=city).exists():
            # City exists, perform further processing
            # For example, retrieve trips for the given city
            trips = Trip.objects.filter(city=city)
            return render(request, 'search_results.html', {'trips': trips})
        else:
            # City does not exist, set invalid_city variable
            return render(request, 'home.html', {'invalid_city': city})
