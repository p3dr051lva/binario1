import math

numero_binario = None
numero_decimal = None

def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)


numero_binario = ''
numero_decimal = float(text_prompt('digite o numero'))
while numero_decimal > 0:
  if numero_decimal % 2 == 0:
    numero_binario = '0' + str(numero_binario)
    numero_decimal = numero_decimal / 2
  else:
    numero_binario = '1' + str(numero_binario)
    numero_decimal = numero_decimal / 2
    numero_decimal = math.floor(numero_decimal)
print(numero_binario)
