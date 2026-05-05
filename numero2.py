distancia_total = 500
distancia_percorrida = 0
hora = 0
while distancia_percorrida < distancia_total:
  hora += 1:
distancia_restante = distancia_total - distancia_percorrida
if distancia_restante < 80:
  distancia_percorrida += distancia_restante
else:
  distancia_percorrida += 80
  falta = distancia_total - distancia_percorrida
  print("hora:", hora)
  print("Distância percorrida:", distancia_percorrida)
  print("Distância restante:", distancia_total - distancia_percorrida)

print("Viagem concluída em", hora, "horas.")
