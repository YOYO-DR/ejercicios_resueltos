#6. Transforma n metros a centímetro.

# con esta funcion valido si un valor es un numero
def esNumero(num):
  try:
    # aqui intento convertirlo a numero, si no sale error, retorna true
    float(num)
    return True
  except:
    # si sale algun error convirtiendo el numero, significa que no es un numero y retorno false
    return False

# pido la cantidad de metros
metros=input("Ingresa la cantidad de metros a convertir: ")

# verifico que sea un numero
if not esNumero(metros):
  print(f"'{metros}' no es un número")
else:
  # si es un numero, lo convierto a flotante
  metros=float(metros)

  # calculo los centimetros, los cuales son los metros por 100
  centimetros=metros*100

  # muestro el resultado
  print(f"{metros} metros son {centimetros} centimetros")