#3. Elevar un número al cubo ingresado por consola. 

# con esta funcion valido si un valor es un numero
def esNumero(num):
  try:
    # aqui intento convertirlo a numero, si no sale error, retorna true
    float(num)
    return True
  except:
    # si sale algun error convirtiendo el numero, significa que no es un numero y retorno false
    return False

#pido el valor
num=input("Ingresa un numero: ")

# verifico que sea un numero
if not esNumero(num):
  print(f"'{num}' no es un número")
else:
  # muestro el resultado
  # convierto el numero a flotante, en la funcion solo pregunte si era numero, y elevo ese número al cubo
  print(f"El resultado de elevar '{num}' al cubo es '{float(num)**3}'")