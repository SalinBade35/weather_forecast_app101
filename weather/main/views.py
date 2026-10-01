import requests
from django.contrib import messages

from django.shortcuts import render


def home(request):
    # Read the searched city, or use Lalitpur on the first visit.
    city = request.POST.get('city', 'lalitpur').strip()

    # OpenWeather needs the city, API key, and metric units.
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': 'fae18650e2e92cb418d830d7e55f7bd8',
        'units': 'metric',
    }

    # These values are sent to index.html after the API request.
    context = {'city': city, 'temp': 0, 'desc': '', 'icon': '', 'wind': 0, 'humidity': 0}

    try:
        # Request the weather data and keep only the values the page needs.
        data = requests.get(url, params=params, timeout=10).json()
        context.update({
            'temp': data['main']['temp'],
            'desc': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
            'wind': data['wind']['speed'],
            'humidity': data['main']['humidity'],
        })
    except (requests.RequestException, KeyError, TypeError, ValueError):
        # Show a friendly message when the city or API response is invalid.
        context['desc'] = 'There is no such city'
        messages.error(request, 'There is no such city')

    # Render the page using the weather values collected above.
    return render(request, 'index.html', context)


