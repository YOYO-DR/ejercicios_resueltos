# 1. Calcular el área y perímetro de un triángulo rectángulo si se conocen los valores de sus catetos, pedirle los 2 catetos al usuario.

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
cat1=input("Ingresa el primer cateto: ")
cat2=input("Ingresa el segundo cateto: ")

# con la funcion valido los valores ingresados
if not esNumero(cat1):
  print(f"'{cat1}' no es un número")
elif not esNumero(cat2):
  print(f"'{cat2}' no es un número")
else:
  # si son numeros, ya los convierto de string a float para poder hacer operaciones con ellos
  cat1=float(cat1)
  cat2=float(cat2)

  # encontrar la hipotenusa
  # hipo^2=cat1^2+cat2^2 pero en python, los exponenciales son con **, y para la raiz, se eleva, en este caso para la raiz (1/2), raiz cubica (1/3) y asi sucesivamente, se sabe que primero se elevan los catetos y luego se suman, y ahi si vendria la raiz de ese resultado
  hipo=((cat1**2)+(cat2**2))**(1/2)

  # calcular area
  # multiplicacion de los catetos divido 2
  # recordar el orden de los parentesis y las operaciones
  area=(cat1*cat2)/2

  # calcular perimetro
  # perimetros es la suma de todos los lados
  peri=cat1+cat2+hipo

  # mostrar resultados
  # el round es para aproximar, en este caso, a 2 decimales
  print(f"La hipotenusa de los catetos ({cat1},{cat2}) es '{round(hipo,2)}'\nEl area del triangulo es '{round(area,2)}'\nEl perimetro del triangulo es '{round(peri,2)}'")

