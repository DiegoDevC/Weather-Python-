import tkinter as tk
import requests

window = tk.Tk()
window.title("App de Temperatura")
window.config(bg="#0080ff")
font = ("Arial", 14)

input_container = tk.Frame(window, bg="#0080ff")
input_container.pack(pady=10)
city_label = tk.Label(input_container, text="Digite a cidade:", font=font, bg="#0080ff", fg="white")
city_label.pack(side="left", padx=10)
city_entry = tk.Entry(input_container, font=font)
city_entry.pack(side="left")


get_temp_button = tk.Button(input_container, text="Obter temperatura", font=font, bg="white")
get_temp_button.pack(side="left", padx=10)
temp_container = tk.Frame(window, bg="#0080ff")
temp_container.pack(pady=20)
temp_label = tk.Label(temp_container, text="", font=font, bg="#0080ff", fg="white")
temp_label.pack()

def get_temperature():
    city = city_entry.get()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=91192deebb79d46c6bd92fec66b28162&units=metric"
    response = requests.get(url)
    weather_data = response.json()
    if "main" in weather_data and "temp" in weather_data["main"]:
        temperature = weather_data["main"]["temp"]
        temp_label.config(text=f"Temperatura atual: {temperature}°C")
    else:
        temp_label.config(text="Cidade não encontrada")
        
get_temp_button.config(command=get_temperature)
window.mainloop()
