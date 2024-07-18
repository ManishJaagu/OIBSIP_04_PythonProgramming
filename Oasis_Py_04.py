''' Author- Jagu Manish || Python Programming Internship at Oasis Infobyte

------------------ TASK 4 - BASIC WEATHER APP  BEGINNER-----------------------
For Beginners: Create a command-line weather app in Python that fetches and displays current weather data for a
 user-specified location (e.g., city or ZIP code) using a weather API. Show basic information such as temperature,
 humidity, and weather conditions.

For Advanced: Develop a graphical weather app with a user-friendly interface (GUI) using libraries like Tkinter or
PyQt. Enable users to input their location or use GPS for automatic detection. Provide detailed weather data, including
current conditions, hourly and daily forecasts, wind speed, and visual elements like weather icons.

 Key Concepts and Challenges:
API Integration: Connect to a weather API and parse JSON data.
User Input Handling: Validate and process user input for location.
GUI Design (for Advanced): Create a user-friendly interface with input fields, weather data displays, and visual elements.
GPS Integration (for Advanced): Implement location detection if developing a mobile app.
Error Handling: Address potential errors during data retrieval or user input.
Data Visualization (for Advanced): Display weather data in an appealing manner, possibly using icons or animations.
Unit Conversion (for Advanced): Offer unit options for temperature (e.g., Celsius and Fahrenheit).


IDE used: Pycharm
Tip: Use VS Code for better performance.

'''
import requests

api_key = '[PASTE YOUR OPEN WEATHER API KEY HERE]'

while True:
    user_input = input("Enter a city name: ").title()

    print(f"Retrieving Weather report of {user_input}. Please wait....")

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

    if weather_data.json()['cod'] == '404':
        print("No city Found!")
    else:
        data = weather_data.json()
        city_longitude = data['coord']['lon']
        city_latitude = data['coord']['lat']
        status = data['weather'][0]['main']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        sea_level_pressure = data['main']['sea_level']
        ground_level_pressure = data['main']['grnd_level']
        wind_speed = data['wind']['speed']
        wind_direction = data['wind']['deg']
        condition = data['weather'][0]['description']

        print(f"\n{user_input}'s Coordinates: Longitude: {city_longitude}º , Latitude: {city_latitude}º")
        print("                              ╔═══════════════════════════════════════════════════════╗")
        print("                              ║          W E A T H E R    C O N D I T I O N S         ║")
        print("                              ╚═══════════════════════════════════════════════════════╝")
        print(f"Status : {status}")
        print(f"Condition: {condition}")
        print(f"Temperature: {temp}ºF")
        print(f"Pressure: {pressure} hPa")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Wind Direction: {wind_direction}º")
        print(f"Humidity: {humidity}%")
        print(f"Sea level Pressure: {sea_level_pressure} hPa")
        print(f"Ground level Pressure: {ground_level_pressure} hPa")

    while True:
        find_again = input("Do you want to try again? (y/n): ").lower()
        if find_again == 'y':
            break
        elif find_again == 'n':
            exit()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
