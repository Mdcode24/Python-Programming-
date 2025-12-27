import requests
from tkinter import*
from PIL import Image,ImageTk


API_KEY="71073fd2531506b8f064ee5f76a722d7"

def get_weather(city):
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response=requests.get(url)
        response.raise_for_status()
        weather_data=response.json()
        return{
            'city':weather_data['name'],
            'temp':weather_data['main']['temp'],
            'humidity':weather_data['main']['humidity'],
            'pressure':weather_data['main']['pressure'],
            'latitude':weather_data['coord']['lat'],
            'longitude':weather_data['coord']['lon']
        }

    except requests.exceptions.RequestException as e:
        print("Error",f"failed:{e}")
        return

class WeatherApp:
    def __init__(self,root):
        self.root=root
        self.root.title("City weather app")
        self.root.geometry('400x400')
        
        self.image=Image.open(r"D:\Python Programming\New Volm E\Phyton programming\Class 8\weather app.png")
        image=self.image.resize((150,200))
        self.photo=ImageTk.PhotoImage(image)
        self.image_label=Label(root,image=self.photo)
        self.image_label.pack(pady=5)
        self.city_label=Label(self.root,text="City:")
        self.city_label.pack(pady=10)
        self.city_entry=Entry(self.root)
        self.city_entry.pack(pady=10)
        self.get_weather_button=Button(self.root,text="Get Weather Display",command=self.display_weather)
        self.get_weather_button.pack(pady=10)
        self.result_label=Label(self.root,text="",font=("Helvetica",12))
        self.result_label.pack(pady=10)

    def display_weather(self):
        city_data=self.city_entry.get()  
        if city_data:
            weather=get_weather(city_data)
            print(weather)
            if  weather:
                self.result_label.config(text=f"Weather in {weather['city']} city is :\n"
                        f"Temperature: {weather['temp']}°C\n"
                        f"Humidity: {weather['humidity']}%\n"
                        f"Pressure: {weather['pressure']} hPa\n"
                        f"Latitude: {weather['latitude']}\n"
                        f"Longitude: {weather['longitude']}\n")
            else:
                self.result_label.config(text="Please enter the city name.")

if __name__=="__main__":
    root=Tk()
    app=WeatherApp(root)
    root.mainloop()
