# 24. Elabora un programa que multiplique dos números enteros positivos utilizando sumas sucesivas (a x b, significa sumar b veces el número a), a y b se le piden al usuario.

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
a=input("Ingresa el primer número: ")
b=input("Ingresa el segundo número: ")

# verificar que sean numeros
if not esNumero(a):
  print(f"'{a}' no es un número entero")
elif not esNumero(b):
  print(f"'{b}' no es un número entero")
else:
  # convertir a número entero
  a=int(a)
  b=int(b)

  # verificar que los numeros no sean negativos o 0
  if a<1:
    print(f"'{a}' no puede ser menor a 1")
  elif b<1:
    print(f"'{b}' no puede ser menor a 1")
  else:
    # sumo el primer numero, 'b' veces 
    res=0
    for x in range(b):
      res+=a
    
    #muestro el resultado
    print(f"'{a}' multiplicado por '{b}' con sumas sucesivas es '{res}'")
