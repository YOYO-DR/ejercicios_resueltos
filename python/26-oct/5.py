# 5. Calcula el IVA (19%) de una cantidad ingresada por el usuario.

# con esta funcion valido si un valor es un numero
def esNumero(num):
  try:
    # aqui intento convertirlo a numero, si no sale error, retorna true
    float(num)
    return True
  except:
    # si sale algun error convirtiendo el numero, significa que no es un numero y retorno false
    return False

# pido la cantidad
cantidad=input("Ingresa la cantidad: ")

# verifico que sea un numero
if not esNumero(cantidad):
  print(f"'{cantidad}' no es un número")
else:
  # si es un numero, lo convierto a flotante
  cantidad=float(cantidad)

  # calculo el iva, el cual es la cantidad por el 19%
  iva=cantidad*0.19

  # muestro el resultado
  print(f"El IVA de '{cantidad}' es '{iva}'")