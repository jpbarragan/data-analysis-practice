import requests

city = input("What city do you want to see the weather for?\n")

url = "http://api.weatherapi.com/v1/current.json?key=10b67c2edf8e4da083e184126240203&q="+city+"&aqi=no"

response = requests.get(url)

json = response.json()

temperature = json.get("current").get("temp_f")
description = json.get("current").get("condition").get("text")

print("The current weather in ", city, " is ", description, " with a temperature of ", temperature, ".", sep="")