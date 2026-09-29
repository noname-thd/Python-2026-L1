import math 

celsius_input = input("Enter the temperature: ")
celsius = float(celsius_input)
fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius_input} (C) = {fahrenheit:.1f} (F)")