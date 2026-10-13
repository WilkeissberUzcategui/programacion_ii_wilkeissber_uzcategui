droides = [
    {
        "codigo": "DR0-001",
        "modelo": "A1",
        "energia": "100",
        "activo": True
    },

    {
        "codigo": "DR0-002",
        "modelo": "B2",
        "energia": "80",
        "activo": True
    },

    {
        "codigo": "DR0-003",
        "modelo": "C3",
        "energia": "60",
        "activo": False
    }
]

# CRUD
# CREATE

cantidad_droides = len(droides)
print(cantidad_droides)
print(droides)

nuevo_droide = {
    "codigo": "DR0-004",
    "modelo": "D4",
    "energia": "90",
    "activo": True
}

droides.append(nuevo_droide)
print(len(droides))
print(droides)

# READ

droide = droides[0]
print(f"Codigo : {droide['codigo']}")
print(f"Modelo : {droide['modelo']}")
print(f"Energia : {droide['energia']}")
print(f"Activo : {droide['activo']}")

# UPDATE

droide = droides[2]
droide["codigo"] = "DR0-002"
droide["energia"] = "0"
droide["activo"] = False
print(f"Droides : {droides}")

# DELETE

eliminado = droides.pop(2)
print(f"droides : {droides}")

