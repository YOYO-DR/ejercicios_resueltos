# 15. Indica si un número entero positivo es primo o no

# con esta funcion valido si un valor es un numero
def esNumero(num):
  try:
    # aqui intento convertirlo a numero, si no sale error, retorna true
    float(num)
    return True
  except:
    # si sale algun error convirtiendo el numero, significa que no es un numero y retorno false
    return False

# pido el numero
num=input("Ingresa un número entero positivo: ")

# verifico que sea un numero
if not esNumero(num):
  print(f"'{num}' no es un número")
else:
  # si es un numero, lo convierto a entero
  num=int(num)

  # verifico que el numero sea positivo
  if num<0:
    print("El número no puede ser negativo")
    # salgo del programa
    exit()

  # si el numero es 1, no es primo
  if num==1:
    print("El número no es primo")
  else:
    # si no, verifico si es primo
    # para eso, recorro todos los numeros desde 2 hasta el numero anterior
    for i in range(2,num):
      # si el numero es divisible entre alguno de los numeros anteriores, no es primo
      # el % es el operador modulo, que retorna el residuo de una division, por ejemplo 10/3 es igual a 3, pero sobra 1, entonces 10%3 es igual a 1
      if num%i==0:
        print("El número no es primo")
        # salgo del programa
        exit()
    # si no, es primo
    print("El número es primo")