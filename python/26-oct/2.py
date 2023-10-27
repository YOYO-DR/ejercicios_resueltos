#2. Dado el costo de un artículo vendido y la cantidad de dinero entregada por el cliente, calcula e imprime el cambio que debe entregársele al mismo. 

# con esta funcion valido si un valor es un numero
def esNumero(num):
  try:
    # aqui intento convertirlo a numero, si no sale error, retorna true
    float(num)
    return True
  except:
    # si sale algun error convirtiendo el numero, significa que no es un numero y retorno false
    return False

#pido los valores
costoArticulo=input("Ingresa el costo del articulo: ")
montoCliente=input("Ingresa el monto del cliente: ")

if not esNumero(costoArticulo):
  print(f"'{costoArticulo}' no es un número")
elif not esNumero(montoCliente):
  print(f"'{montoCliente}' no es un número")
else: 
  # si son numeros, ya los convierto de string a float para poder hacer operaciones con ellos
  costoArticulo=float(costoArticulo)
  montoCliente=float(montoCliente)

  # calcular cambio
  cambio=montoCliente-costoArticulo

  # mostrar resultados
  # el round es para aproximar, en este caso, a 2 decimales
  print(f"El cambio es ${round(cambio,2)}")