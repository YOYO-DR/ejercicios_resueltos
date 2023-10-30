from random import randint
# 20. Realizar la lectura de una lista de números y determinar cuántos son positivos, y cuántos son negativos.

# creare una lista con números 20 aleatorios

# hago un for con 20 vueltas, y en cada vuelta agrego un numero aleatorio entre -100 y 100, y eso me lo da la funcion randint
# esta es una forma
lista_numeros=[randint(-100,100) for x in range(20)]

# esta es otra
# inicializamos la lista
# lista_numeros=[]
# for x in range(20):
#   lista_numeros.append(randint(-100,100))

# inicializar los contadores de numeros positivos y negativos
positivos=0
negativos=0

# recorrer los numeros
for num in lista_numeros:
  # pregunto si un numero es positivo (mayor a 0) y sumo el contador, de lo contrario, sumo el contador de negativos
  if num>0:
    positivos+=1
  else:
    negativos+=1

# muestro los resultados
print(f"En la lista de nnúmeros:\n{lista_numeros}\nExisten {positivos} números positivos y {negativos} números negativos")