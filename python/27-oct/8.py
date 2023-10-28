#8. Realiza un programa que efectúe la transformación de horas a minutos.

# con esta funcion valido si un valor es un numero
def esNumero(num):
  try:
    # aqui intento convertirlo a numero, si no sale error, retorna true
    float(num)
    return True
  except:
    # si sale algun error convirtiendo el numero, significa que no es un numero y retorno false
    return False

# pedir las horas
horas=input("Ingresa las horas a convertir: ")

# verifico que sea un numero
if not esNumero(horas):
  print(f"'{horas}' no es un número")
else:
  # si es un numero, lo convierto a flotante
  horas=float(horas)

  # calculo los minutos, los cuales son las horas por 60
  minutos=horas*60

  # muestro el resultado
  print(f"{horas} horas son {minutos} minutos")