# Transporte Público

Tema: Transporte público.

# Tablas

- Parada (nombre, direccion)
- Conductor (nombre, licencia, fecha_ingreso)
- Ruta (nombre, origen, destino, distancia, tarifa, paradas, creado_por)
- Vehiculo (placa, tipo, capacidad, activo, ruta, conductor, creado_por)

# Levantar el proyecto
    
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py cargar_datos
python manage.py runserver

# Usuarios de prueba

| Usuario | Grupo | Contraseña |
|---|---|---|
| admin | superusuario | Admin12345 |
| administrador1 | administradores | Admin12345 |
| consultor1 | consultores | Consultor12345 |