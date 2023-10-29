# 14. Una tienda de deportes vende pelotas de béisbol a $10 cada una, si se compran menos de 5, y a $14, si se compran 5 o más; se quiere saber el costo total de la compra, dependiendo del número de pelotas solicitadas.

# con esta funcion valido si un valor es un numero
def esNumero(num):
  try:
    # aqui intento convertirlo a numero, si no sale error, retorna true
    float(num)
    return True
  except:
    # si sale algun error convirtiendo el numero, significa que no es un numero y retorno false
    return False

# pedir la cantidad de pelotas
cantidad=input("Ingresa la cantidad de pelotas a comprar: ")

# verifico que sea un numero
if not esNumero(cantidad):
  print(f"'{cantidad}' no es un número")
else:
  # si es un numero, lo convierto a flotante
  cantidad=float(cantidad)

  # verifico que la cantidad no sea negativa
  if cantidad<0:
    print("La cantidad no puede ser negativa")
    # salgo del programa
    exit()

  # si la cantidad es menor a 5
  if cantidad<5:
    # el precio es de 10
    precio=10
  else:
    # si no, es de 14
    precio=14

  # muestro el precio
  print(f"El precio total es ${precio*cantidad}")