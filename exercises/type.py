width = 17
height = 12.0

print(type(width//2))
print(type(width/2.0))
print(type(height/3))


# Write a program which prompts the user for a Celsius temperature, 
# convert the temperature to Fahrenheit, and print out the converted temperature.

temp = float(input('Enter the temperature in Celcius: '))
converter = (temp * 1.8) + 32

print('{}°C converted to fahrenheit is {}°F'.format(temp, converter))