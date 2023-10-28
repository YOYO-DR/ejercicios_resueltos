# 10. Aplicar un aumento de 15% a un trabajador si su sueldo es inferior a $1000 mensuales y 12% en caso contrario.

# con esta funcion valido si un valor es un numero
def esNumero(num):
  try:
    # aqui intento convertirlo a numero, si no sale error, retorna true
    float(num)
    return True
  except:
    # si sale algun error convirtiendo el numero, significa que no es un numero y retorno false
    return False

# pedir el sueldo
sueldo=input("Ingresa el sueldo del trabajador: ")

# verifico que sea un numero
if not esNumero(sueldo):
  print(f"'{sueldo}' no es un número")
else:
  # si es un numero, lo convierto a flotante
  sueldo=float(sueldo)

  # si el sueldo es menor a 1000
  if sueldo<1000:
    # los porcentajes se muestran siempre de 0.01 (1%) a 1 (100%)
    # aumento el sueldo en un 15%
    sueldo+=sueldo*0.15
  else:
    # aumento el sueldo en un 12%
    sueldo+=sueldo*0.12
  
  # muestro el sueldo
  print(f"El sueldo del trabajador es {round(sueldo,2)}")