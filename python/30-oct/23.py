# 23. Solicitar al usuario el ingreso de una contraseña desde el teclado. El programa deberá continuar su ejecución hasta que la contraseña sea correcta.

# guardo la contraseña correcta
contra="admin2003"

# pregunto por la contraseña, si es correcta termino el programa, de lo contrario, inicio el ciclo para pedirle la contraseña varias veces
ingreso=input("Ingrese la contraseña: ")
if ingreso==contra:
  print("¡Inicio de sesión correcto!")
else:
  # hago el ciclo infinito hasta que ingrese la contraseña correcta
  while True:
    # le digo que es incorrecta y la pido de nuevo
    ingreso=input("Contraseña incorrecta, ingresala de nuevo: ")
    if ingreso!=contra:
      # si sigue siendo diferente, pongo "continue" para que siga en el ciclo
      continue
    else:
      # de lo contrario ya lo saco del ciclo
      print("¡Inicio de sesión correcto!")
      break
