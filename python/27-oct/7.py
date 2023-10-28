#7. Realiza el promedio de 4 calificaciones de una misma materia.

# con esta funcion valido si un valor es un numero
def esNumero(num):
  try:
    # aqui intento convertirlo a numero, si no sale error, retorna true
    float(num)
    return True
  except:
    # si sale algun error convirtiendo el numero, significa que no es un numero y retorno false
    return False

# pido las calificaciones, las guardare en un arreglo
calificaciones=[]

# con range le digo cuantas vueltas quiero dar, en este casi 4, va a ir de 0 a 3
for i in range(4):
  # pido la calificacion, le sumo 1 para mostrar pq inicia en 0
  calificacion=input(f"Ingresa la calificacion {i+1}: ")

  # verifico que sea un numero
  if not esNumero(calificacion):
    print(f"'{calificacion}' no es un número")
    # si no es un numero, con break detengo el ciclo
    break
  else:
    # si es un numero, lo convierto a flotante y lo agrego al arreglo
    calificaciones.append(float(calificacion))

# verifico que las calificaciones sean 4, pq si son menos, significa que ingreso un valor que no es un numero
if len(calificaciones)<4:
  # con exit detengo la ejecucion del programa
  exit()

# obtengo la suma de los arreglos
suma=0
# recorro las calificaciones, el valor va a ser cada valor del arreglo en cada vuelta
for valor in calificaciones:
  suma+=valor # y como lo guarde convertido a flotante, puedo sumarlo

# obtengo el promedio, que es la suma de las calificaciones entre la cantidad de calificaciones
promedio=suma/len(calificaciones)

# muestro el resultado, lo redondeo ya que lo dividi y pueden salir varios decimales
print(f"El promedio de las calificaciones es {round(promedio,2)}")