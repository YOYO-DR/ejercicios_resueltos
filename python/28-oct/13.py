# 13. Una escuela tiene el siguiente problema: si el alumno obtiene una calificación de menos de 65 puntos no aprobará el curso, en otro caso lo aprobará. Pedir la nota al usuario

# con esta funcion valido si un valor es un numero
def esNumero(num):
  try:
    # aqui intento convertirlo a numero, si no sale error, retorna true
    float(num)
    return True
  except:
    # si sale algun error convirtiendo el numero, significa que no es un numero y retorno false
    return False

# pedir calificacion del estudiante
calificacion=input("Ingresa la calificación del estudiante: ")

# verifico que sea un numero
if not esNumero(calificacion):
  print(f"'{calificacion}' no es un número")
else:
  # si es un numero, lo convierto a flotante
  calificacion=float(calificacion)

  # verifico que la calificacion no sea negativa
  if calificacion<0:
    print("La calificación no puede ser negativa")
    # salgo del programa
    exit()

  # si la calificacion es menor a 65
  if calificacion<65:
    # reprobo
    print("El estudiante reprobo")
  else:
    # aprobo
    print("El estudiante aprobo")