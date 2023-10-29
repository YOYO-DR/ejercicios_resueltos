# 12. Los conjuntos deportivos tienen un precio de $500 cada uno si se compran menos de 3, y de 450 si se compran 3 o más. Obtener el total a pagar dependiendo del número de conjuntos a comprar.

# con esta funcion valido si un valor es un numero
def esNumero(num):
  try:
    # aqui intento convertirlo a numero, si no sale error, retorna true
    float(num)
    return True
  except:
    # si sale algun error convirtiendo el numero, significa que no es un numero y retorno false
    return False


# pedir la cantidad de conjuntos
cantidad=input("Ingresa la cantidad de conjuntos a comprar: ")

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

  # si la cantidad es menor a 3
  if cantidad<3:
    # el precio es de 500
    precio=500
  else:
    # si no, es de 450
    precio=450

  # muestro el precio
  print(f"El precio total es ${round(precio*cantidad,2)}")
