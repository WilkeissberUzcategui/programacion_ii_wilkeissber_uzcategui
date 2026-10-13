# ciclo for

naves = [
    "Caza n-1",
    "Nave real de Naboo", 
    "Transporte"]

for nave in naves:
    print("Inspeccionando ", nave)
    
print("Inspección realizada")

rondas = range(1, 6)

print("Tipo de rondas: ", type(rondas))
for ronda in rondas:
    print(f"Ronda de vigilancia {ronda}")
    print(f" Tipo de ronda: {type(ronda)}")
    
print("-" * 50)    

droides = range(1, 17, 3)

print("Tipo de droides: ", type(droides))
for droide in droides:
    print(f"reparar: droide b1-{droide}")
    print(f" Tipo de dato droide: {type(droide)}")
    
print("-" * 50)

planetas = [
    "Naboo",
    "Tatooine",
    "Coruscant",
]

recorrido = enumerate(planetas, start=5)

for posicion, planeta in recorrido:
    print(f"Destino {posicion} : {planeta}")
    print(f" Tipo de dato: {type(posicion)} : {type(planeta)}")
    
print("-" * 50)

paises = [
    "Ecuador",
    "Venezuela",
    "Chile",
    "Colombia",
    "Brasil",
    "Estados Unidos",
]

for pais in paises:
    if pais == "Chile":
        continue
    if pais == "Brasil":
        break
    print(f"País visitado: {pais}")
    
print("-" * 50)

jedi = {}
jedi_activos = {
    "nombre": "Obi-Wan",
    "fuerza": "120",
    "estilo_pelea": "Samurai",
    "misiones": ["Guerra alderan", "Secuestro palpatine", "Escolta de leia"],
    "descripcion": {
        "estatura": 1.80,
        "especie": "humana",
    }
}

print(jedi_activos)
nave = dict(nombre = "AZ-1", capacidad = 8, turbo_laser = 2)
print(nave)

jedi["nombre"] = "Luck"
jedi["fuerza"] = 100
print(jedi)

print("-" * 50)

for clave, valor in jedi_activos.items():
    print(f"{clave} - {valor}")