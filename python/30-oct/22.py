# 22. Modifica el ejercicio anterior para que imprima los números impares.

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

# pedir los 2 numeros
a=input("Ingresa el primer número entero: ")
b=input("Ingresa el segundo número entero (debe ser mayor al anterior): ")

# verificar que sean enteros
if not esNumeroEntero(a):
  print(f"'{a}' no es un número entero")
elif not esNumeroEntero(b):
  print(f"'{b}' no es un número entero")
else:
  # convierto a entero
  a=int(a)
  b=int(b)

  # verifico que el segundo numero sea mayor al primero
  if a>b:
    print(f"El primer numero ({a}) no puede ser mayor al segundo numero ({b})")
  else:
    # hago el for y guardo la lista de impares
    impares=[]

    # le digo que va a iniciar desde a y terminar en b, le sumo 1 pq siempre va a llegar al numero anterior de b
    for num in range(a,b+1):
      # pregunto si el numero es 0, para no agregarlo a la lista
      if num==0:
        # la sentencia "continue" le digo que no lea el codigo siguiente del for y salte a la siguiente vuelta
        continue
      if num%2!=0:
        # si su modulo o residuo da 1 o diferente a 0, al dividido entre 2, entonces es impar
        impares.append(num)
    
    # muestro el resultado
    print(f"Los números impares entre '{a}' y '{b}' son:\n{impares}")
