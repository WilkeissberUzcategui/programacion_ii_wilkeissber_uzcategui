'''
Control de Flota de Naboo
'''

naves = [
    {
        "nombre": "Caza n-1",
        "combustible": 80,
        "droides": ["R2-D2", "R2-A6"],
    },
    {
        "nombre": "Caza REal",
        "combustible": 35,
        "droides": ["R2-D2", "R2-N3"],
        },
    {
        "nombre": "Transporte",
        "combustible": 65,
        "droides": ["R2-D2", "R2-A3"],
        },
]

naves_lista = 0
naves_recargadas = 0
total_droides = 0
total_ciclos = 0

for numero, nave in enumerate(naves, start=1):
    print(f"--- Nave : {numero} - {nave}")
    if nave["combustible"] >=50:
        print("Estado inicial: LISTA")
        naves_lista += 1
    else:
        print("Estado inicial: RECARGAR")
        naves_recargadas += 1
        ciclo = 0
        while nave["combustible"] <= 50:
            ciclo += 1
            nave["combustible"] += 10
        total_ciclos += ciclo
        print("Recarga completada")
        print("Estado Final: LISTA")
    total_droides += len(nave["droides"])
    for droide in nave["droides"]:
        print(f"droide: {droide}")
        
print("=" * 50)
print("Resumen")
print("=" * 50)
print(f"Total Naves {len(nave)}")
print(f"Naves Listas Iniciadas {naves_lista}")
print(f"Naves Recargadas: {naves_recargadas}")
print(f"Total Droides: {total_droides}")
print(f"Total Ciclos: {total_ciclos}")