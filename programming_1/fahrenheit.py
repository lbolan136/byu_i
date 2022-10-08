"""
Converts a temperature entered in Fahrenheit to Celsius.
Author Logan Bolan

"""

temp_fahrenheit = float(input("What is the temperature in Fahrenheit? "))
temp_celsius = ( temp_fahrenheit - 32 ) * 5 / 9

print(f"The temperature in Celsius is {temp_celsius:.1f} degrees.")