import tkinter as tk
import requests
import time


def getWeather(canvas):
    city = textField.get()    
    key = 'bfd4d881d107ea98695bf70aade537fb'
    api = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}'

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(
        json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(
        json_data['sys']['sunset'] - 21600))

    condition_info = condition
    temp_info = f"{temp}°C"

    final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" + "\n" + "Pressure: " + str(
        pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text=condition_info)
    label3.config(text=temp_info)
    label2.config(text=final_data)



canvas = tk.Tk()
canvas.geometry("600x450")
canvas.title("Weather App - Search by City")
l = ("Ava Meridian", 35, "bold")
m = ("Ava Meridian", 25, "bold")
s = ("poppins", 15, "bold")
xs = ("poppins", 10, "italic")


textField = tk.Entry(canvas, justify='center',
                     width=20, font=m)
textField.pack(pady=20, padx=20)
textField.focus()
textField.bind('<Return>', getWeather)

label = tk.Label(canvas, font=xs)
label.pack()
label.config(text="e.g: ho chi minh, ha noi", padx=6, pady=4)

label1 = tk.Label(canvas, font=l)
label1.pack()
label3 = tk.Label(canvas, font=m)
label3.pack()
label2 = tk.Label(canvas, font=s)
label2.pack()

canvas.mainloop()
