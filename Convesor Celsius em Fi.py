import time
import os

print ("CONVERSOR DE TEMPERATURA °C PARA °F")
time.sleep(4)
os.system ("cls")
print("By Gabriel Ricardo =)")
time.sleep(4)
os.system ("cls")
tempc = float(input ("Informe sua Temperatura em °C: "))
f= ((9*tempc)/5)+32
print ("{}°C em Celsius é {}°F em Fahrenheit".format(tempc, f))
time.sleep (4)
os.system ("cls")