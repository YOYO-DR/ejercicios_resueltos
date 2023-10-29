# 11. Calcular el precio de un boleto de ida y vuelta en ferrocarril, conociendo la distancia del viaje de ida y el tiempo de estancia. Se sabe, además, que si el número de días de estancia es superior a 7 y la distancia total (ida y vuelta) a recorrer es superior a 800 km, el boleto tiene un descuento del 30%. El precio por kilómetro es $0.25

# con esta funcion valido si un valor es un numero
def esNumero(num):
  try:
    # aqui intento convertirlo a numero, si no sale error, retorna true
    float(num)
    return True
  except:
    # si sale algun error convirtiendo el numero, significa que no es un numero y retorno false
    return False

# pedir los kilometros recorridos (ida y vuelta) y el tiempo (que seria en dias)
kilometros=input("Ingresa los kilometros recorridos (ida y vuelta): ")
tiempo=input("Ingresa el tiempo de estancia (en dias): ")

# verifico que sean numeros
if not esNumero(kilometros):
  print(f"'{kilometros}' no es un número")
elif not esNumero(tiempo):
  print(f"'{tiempo}' no es un número")
else:
  # si son numeros, los convierto a flotantes
  kilometros=float(kilometros)
  tiempo=float(tiempo)

  # calculo el precio por kilometro
  precio=0.25*kilometros

  # si el tiempo es mayor a 7 y los kilometros son mayores a 800
  if tiempo>7 and kilometros>800:
    # aplico el descuento del 30%
    precio-=precio*0.3
  
  # muestro el precio
  print(f"El precio del boleto es ${round(precio,2)}")