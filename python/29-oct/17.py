# 17. Si una persona (Antonio) deposita $1000 al 8% y otra (Marco) deposita $2000 al 3%, ¿cuántos años deberán pasar para que Antonio tenga más dinero que Marco?

# inicializo los valores
antonio=1000
marco=2000
anios=0

# hago un while infinito contando los años que pasan, aumentando los % hasta que antonio revase a marco en dinero

while True:
  # aumento un año porque aumento los porcentajes
  anios+=1
  # recorar los porcentajes de 0.01 (1%) a 1 (100%)
  antonio+=antonio*0.08
  marco+=marco*0.03

  # pregunto si antonio tiene más que marco, si tiene mas, detengo el programa, de lo contario, lo dejo seguir
  if antonio>marco:
    break

# despues del ciclo, mostrar los años
print(f"Pasaron {anios} años para que Antonio revase a Marco")
