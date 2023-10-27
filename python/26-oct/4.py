#4. Calcular el costo total de la compra de cierta cantidad de bates de béisbol cuyo costo es de $10 

# con esta funcion valido si un valor es un numero
def esNumero(num):
  try:
    # aqui intento convertirlo a numero, si no sale error, retorna true
    float(num)
    return True
  except:
    # si sale algun error convirtiendo el numero, significa que no es un numero y retorno false
    return False

#pido la cantidad de bates
cantidadBates=input("Ingresa la cantidad de bates: ")

# verifico que sea un numero
if not esNumero(cantidadBates):
  print(f"'{cantidadBates}' no es un número")
else:
  # si es un numero, lo convierto a flotante
  cantidadBates=float(cantidadBates)

  # calculo el costo total, el cual es el valor por la cantidad de bates ingresados
  costoTotal=cantidadBates*10

  # muestro el resultado
  print(f"El costo total de la compra de '{cantidadBates}' bates de béisbol es ${costoTotal}")