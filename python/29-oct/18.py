# 18. Dado un número, obtenga la sumatoria de dicho número. (La sumatoria de un número n está dada por la suma consecutiva de todos los números hasta n; por ejemplo: sumatoria de 3 es igual a sumar 3+2+1).

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
    # sumo los valores desde el numero hasta 1
    sumatoria=0
    # en el range(num,0,-1) le estoy diciento que inicie desde el numero que le pase, hasta 0 en paso de -1, porque necesito sumar desde el numero hasta 1, y decirle que vaya desde el numero ingresado hasta 0, la verdad no llega hasta 0, llega hasta el numero anterior, en este caso 1, porque vamos en pasos de -1, por ejemplo si se ingresa 3, se va a desde 3 hasta 1 practicamente
    for numero in range(num,0,-1):
      sumatoria+=numero
  
  # muestro el resultado
  print(f"La sumatoria de {num} es: {sumatoria}")
  