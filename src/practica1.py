# Libreria para manejar con json
import json

# Cargar el archivo Práctica1.json en la variable f1
datos = json.load(open("datos.json"))
print()
# Ver los datos cargados (5 accesos diferentes)
#1
print(f"""La escuderia {datos["escuderia"]} la cual empezó en la f1
en el año {datos["creacion"]}, cuyo jefe de equipo es {datos["jefe"]}, han ganado
{datos["constructores"]} campeonatos de constructores.\n""")

#2
print(f"La escuderia {datos["escuderia"]}, tiene dos pilotos: {datos["piloto1"]["nombre"]} y {datos["piloto2"]["nombre"]}\n")

#3
print(f"""El piloto {datos["piloto1"]["nombre"]}:
Ha ganado {datos["piloto1"]["victorias"]} gran premios. 
Ha corrido {datos["piloto1"]["gpCorridos"]} carreras.
Ha conseguido {datos["piloto1"]["puntos"]} puntos.
Ha conseguido {datos["piloto1"]["podios"]} poles.
Y ha corrido para {datos["piloto1"]["equipos"][0]}, {datos["piloto1"]["equipos"][1]} y {datos["piloto1"]["equipos"][2]}\n""")

#4
print(f"""El piloto {datos["piloto2"]["nombre"]}:
Ha ganado {datos["piloto2"]["victorias"]} gran premios. 
Ha corrido {datos["piloto2"]["gpCorridos"]} carreras.
Ha conseguido {datos["piloto2"]["puntos"]} puntos.
Ha conseguido {datos["piloto2"]["podios"]} podios
Y ha corrido para {datos["piloto2"]["equipos"][0]}, {datos["piloto2"]["equipos"][1]}, {datos["piloto2"]["equipos"][2]}, {datos["piloto2"]["equipos"][3]} y {datos["piloto2"]["equipos"][4]}\n""")

#5
print(f"De los dos pilotos, {datos["piloto2"]["nombre"]} es mi favorito, aunque preferiria que continuase en {datos["piloto2"]["equipos"][3]}")