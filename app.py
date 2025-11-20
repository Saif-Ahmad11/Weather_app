from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

API_KEY =
os.getenv('OPENWEATHER_API_KEY')  #Get key from environment

@app.route('/')
def home():
    return render_template('index.html', weather=None, error=None)

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    current_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    forecast_url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric'

    try:
        # Get current weather
        current_response = requests.get(current_url).json()
        if current_response.get("cod") != 200:
            raise ValueError(current_response.get("message"))

        # Get forecast data
        forecast_response = requests.get(forecast_url).json()
        forecast_list = forecast_response['list']

        # Extract next 24-hour forecast (next 8 entries, each 3 hours apart)
        next_8_hours = forecast_list[:8]

        temps = [entry['main']['temp'] for entry in next_8_hours]
        min_temp = min(temps)
        max_temp = max(temps)

        weather = {
            'city': city.title(),
            'temperature': current_response['main']['temp'],
            'feels_like': current_response['main']['feels_like'],
            'humidity': current_response['main']['humidity'],
            'wind_speed': current_response['wind']['speed'],
            'description': current_response['weather'][0]['description'].title(),
            'icon': current_response['weather'][0]['icon'],
            'temp_min': min_temp,
            'temp_max': max_temp,
            'timestamp': datetime.now().strftime("%d %b %Y | %I:%M %p")
        }

        return render_template('index.html', weather=weather, error=None)
    except Exception as e:
        return render_template('index.html', weather=None, error=str(e))

if __name__ == '__main__':
    app.run(port=5001)
