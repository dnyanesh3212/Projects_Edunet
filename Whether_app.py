import streamlit as st
import requests

# OpenWeatherMap API Key
API_KEY = 'ca60b443558bec0e3c7638e5eb271309'

# Function to get weather data
def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'humidity': data['main']['humidity'],
            'pressure': data['main']['pressure'],
            'wind_speed': data['wind']['speed'],
            'visibility': data['visibility'] / 1000 if 'visibility' in data else 'N/A',
            'sunrise': data['sys']['sunrise'],
            'sunset': data['sys']['sunset'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon']
        }
        return weather
    else:
        return None

# Streamlit app
def main():
    st.title('🌍 Advanced Weather App ☀️🌧️')
    st.write('Enter a city name to get detailed weather information.')

    city = st.text_input('🏙️ City Name')

    if city:
        weather = get_weather(city)
        if weather:
            st.write(f"## 📍 {weather['city']}")
            st.write(f"🌡️ **Temperature:** {weather['temperature']}°C")
            st.write(f"🥶 **Feels Like:** {weather['feels_like']}°C")
            st.write(f"☁️ **Weather:** {weather['description'].capitalize()}")
            st.write(f"💧 **Humidity:** {weather['humidity']}%")
            st.write(f"🌀 **Wind Speed:** {weather['wind_speed']} m/s")
            st.write(f"🌅 **Sunrise:** {weather['sunrise']}")
            st.write(f"🌇 **Sunset:** {weather['sunset']}")
            st.write(f"🚦 **Visibility:** {weather['visibility']} km")
            st.write(f"📊 **Pressure:** {weather['pressure']} hPa")
            
            icon_url = f"http://openweathermap.org/img/w/{weather['icon']}.png"
            st.image(icon_url, width=100)
        else:
            st.write("❌ City not found. Please enter a valid city name.")

if __name__ == '__main__':
    main()
