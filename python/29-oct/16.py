#16. Obtener la suma de todos los números enteros pares y la suma de los números impares comprendidos entre 1 y N, en donde N es un entero positivo.

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
  if num<2:
    print("Debe ingresar un número mayor a 1")
  else:
    # realizo la suma entre los pares e impares
    pares=0
    impares=0
    for numero in range(num):
      # como siempre inicia contando por el 0, le sumo 1 para hacer el conteo desde 1 hasta el numero ingresado
      if (numero+1)%2==0: # si su residuo es 0, significa que par, de lo contrario impar
        pares+=numero+1
      else:
        impares+=numero+1
    
    # muestro el resultado
    print(f"Entre 1 y {num}, la suma de los números pares es {pares}, y de los números impares es {impares}")