from machine import ADC
from math import log
from time import sleep

adc = ADC(28)
escalon_tension = 3.3/65535
beta = 3950

while True:
  lectura = adc.read_u16()
  print("El valor del ADC es: {}" .format(lectura))
  tension = escalon_tension * lectura
  print("El valor de tensión es: {}" .format(tension))
  Rntc = (tension*10000)/(3.3-tension)
  print("El valor de la resistencia del NTC es: {}".format(Rntc))
  logaritmo = log(Rntc/10000)
  temperatura = 1/((logaritmo/beta) + 1/298) - 273
  print("El valor de temperatura es: {}" .format(temperatura))
  sleep(1.5)

