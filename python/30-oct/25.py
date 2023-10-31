# 25. Elabora un programa que calcule la parte entera de la división de dos números enteros positivos utilizando restas sucesivas.(a/b)

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
    # guardo una copia de a para mostrar el resultado, porque 'a' se va  modificar
    a_copia=a
    # como en una division, debo restar el segundo numero, al primer numero e ir sumando las vueltas, si la resta llega a ser menor a 0, ahi se detiene la iteracion y ese seria el resultado entero
    res=0
    while True:
      # si al restar el segundo numero, al primer numero NO da un valor menor a 0, sumo 1 al resultado pq eso seria el cociente, de lo contrario, osea si es menor a 0, no sumo nada y salgo del buble
      a=a-b
      if not a<0:
        res+=1
      else:
        break
    
    # muestro el resultado
    print(f"'{a_copia}' dividido '{b}' con restas sucesivas, da como resultado '{res}'")