#9. Convertir una cantidad de metros a kilómetros, centímetros, milímetros y millas, según selección del usuario

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

  # le pregunto al usuario a que quiere convertir los metros
  print("¿A que quieres convertir los metros?\n1. Kilometros\n2. Centimetros\n3. Milimetros\n4. Millas")
  opcion=input("Ingresa la opcion: ")

  #para guardar la converion
  conversion=0
  # para guardar a que lo convirtio
  nombreConversion=""
  # dependiendo de la opcion realizo la conversion
  if opcion=="1":
    #convierto los metros a kilometros, los cuales son los metros divididos 1000
    conversion=metros/1000
    nombreConversion="kilometros"
  elif opcion=="2":
    # convierto los metros en centimetros, los cuales son los metros por 100
    conversion=metros*100
    nombreConversion="centimetros"
  elif opcion=="3":
    # convierto los metros en milimetros, los cuales son los metros por 1000
    conversion=metros*1000
    nombreConversion="milimetros"
  elif opcion=="4":
    # convierto los metros en millas, los cuales son los metros divididos 1609.34
    conversion=metros/1609.34
    nombreConversion="millas"
  else:
    # si no pone una opcion de la lista, le digo que la opcion es invalida
    print("Opcion invalida")
    # detengo el programa
    exit()
  
  # muestro el resultado
  print(f"La conversion de los {metros} metros a {nombreConversion} es {round(conversion,5)} {nombreConversion}")