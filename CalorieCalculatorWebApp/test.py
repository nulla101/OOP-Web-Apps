from calorie import Calorie
from temperature import Temperature

weight = input("Weight: ")
height = input("Height: ")
age = input("Age: ")
country = input("Country: ")
city = input("City: ")

temperature = Temperature(country=country, city=city)

print("Temperature: ", temperature.get())

calories = Calorie(weight=weight, height=height, age=age, temperature=temperature)

print("Calories: ", calories.calculate())
