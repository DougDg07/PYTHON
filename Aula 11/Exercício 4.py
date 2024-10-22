#Faça um program que tenha uma função chamada converter. Essa função deve receber uma temperatura em celcius e retronar em Fahreinheit.

#Conversão de Celsius para Fahrenheit
def converter(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

temperatura_celsius = float(input("Digite a temperatura em graus celsius: "))
temperatura_fahrenheit = converter(temperatura_celsius)
print(f"{temperatura_celsius}°C é igual a {temperatura_fahrenheit}°F.")

#Conversão de Celsius para Kelvin
def converter(celsius):
    kelvin = (celsius + 273)
    return kelvin

temperatura_celsius = float(input("Digite a temperatura em graus celsius: "))
temperatura_kelvin = converter(temperatura_celsius)
print(f"{temperatura_celsius}°C é igual a {temperatura_kelvin}°K.")

#Conversão de Fahrenheit para Kelvin
def converter(fahrenheit):
    kelvin = (fahrenheit + 459,67/ 1.8)
    return kelvin

temperatura_fahrenheit = float(input("Digite a temperatura em graus fahrenheit: "))
temperatura_kelvin = converter(temperatura_fahrenheit)
print(f"{temperatura_fahrenheit}°F é igual a {temperatura_kelvin}°K.")