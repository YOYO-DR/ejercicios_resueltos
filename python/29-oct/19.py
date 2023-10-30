# 19. Calcular la suma de los primeros n números enteros positivos

# con esta funcion valido si un valor es un numero
def esNumero(num):
  try:
    # aqui intento convertirlo a numero, si no sale error, retorna true
    float(num)
    return True
  except:
    # si sale algun error convirtiendo el numero, significa que no es un numero y retorno false
    return False


# con esta funcion valido si un numero es entero
def esNumeroEntero(num):
  # verifico que sea un numero, si es un numero, continua normal
  if not esNumero(num):
    return False
  num=float(num)

  # La funcion int me retorna la parte entera de un numero
  # resto el numero, con su parte entera, si da 0 significa que si es entero (10-int(10)=0), pero si es un flotante osea, tiene decimal (10.5-int(10.5)=0.5), da 0.5 porque int saca la parte entera que es 10 y al darme ese resultado, sabemos que no es entero
  if num-int(num)==0:
    return True
  else:
    return False

# pedir el numero
num=input("Ingresa un número entero positivo: ")

# verifico que sea un entero
if not esNumeroEntero(num):
  print("Debe ingresar un numero entero")
else:
  # lo convierto a entero
  num=int(num)

  # verifico que sea mayor a 0
  if num<1:
    print("Debe ingresar un número mayor a 0")
  else:
    # sumo los valores
    suma=0
    for numero in range(num):
      # le sumo +1 porque como iniciar desde 0, sumandole uno es como su iniciara de 1 que es lo que necesito
      suma+=numero+1
  
  # muestro el resultado
  print(f"La suma es: {suma}")