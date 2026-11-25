from datetime import date
from decimal import Decimal

from django.contrib.auth.models import User, Group, Permission
from django.core.management.base import BaseCommand

from transporte import Parada, Conductor, Ruta, Vehiculo


class Command(BaseCommand):
    help = 'Crea grupos, usuarios de prueba y datos de ejemplo'

    def crear_usuario(self, username, password, grupo=None, superusuario=False):
        user = User.objects.filter(username=username).first()
        if user is None:
            correo = f'{username}@ejemplo.com'
            if superusuario:
                user = User.objects.create_superuser(username, correo, password)
            else:
                user = User.objects.create_user(username, correo, password)
        if grupo:
            user.groups.add(grupo)
        return user

    def handle(self, *args, **options):
        # Grupos y permisos
        administradores, _ = Group.objects.get_or_create(name='administradores')
        consultores, _ = Group.objects.get_or_create(name='consultores')

        permisos = Permission.objects.filter(content_type__app_label='transporte')
        administradores.permissions.set(permisos)
        consultores.permissions.set(permisos.filter(codename__in=[
            'view_parada', 'view_conductor', 'view_ruta', 'view_vehiculo',
            'add_ruta', 'change_ruta',
        ]))

        # Usuarios
        self.crear_usuario('admin', 'Admin12345', superusuario=True)
        administrador = self.crear_usuario('administrador1', 'Admin12345', administradores)
        consultor = self.crear_usuario('consultor1', 'Consultor12345', consultores)

        # Paradas
        datos_paradas = [
            ('Terminal Norte', 'Av. Principal 100'),
            ('Plaza Central', 'Calle 10 y Av. 5'),
            ('Mercado Sur', 'Calle 25 y Av. 8'),
            ('Hospital General', 'Av. Salud 300'),
            ('Universidad', 'Av. Estudiantes 50'),
        ]
        paradas = [Parada.objects.get_or_create(nombre=n, defaults={'direccion': d})[0]
                   for n, d in datos_paradas]

        # Conductores
        datos_conductores = [
            ('Carlos Mora', 'LIC-001', date(2020, 3, 15)),
            ('Ana Pérez', 'LIC-002', date(2021, 6, 1)),
            ('Luis Torres', 'LIC-003', date(2019, 9, 20)),
            ('María Gómez', 'LIC-004', date(2022, 1, 10)),
            ('Jorge Ruiz', 'LIC-005', date(2023, 5, 5)),
        ]
        conductores = [Conductor.objects.get_or_create(
            licencia=lic, defaults={'nombre': n, 'fecha_ingreso': f})[0]
            for n, lic, f in datos_conductores]

        # Rutas
        rutas = []
        for i in range(1, 6):
            ruta, _ = Ruta.objects.get_or_create(
                nombre=f'Ruta {i}',
                defaults={
                    'origen': 'Norte',
                    'destino': 'Sur',
                    'distancia': Decimal('10.50') + i,
                    'tarifa': Decimal('0.35'),
                    'creado_por': administrador if i <= 3 else consultor,
                })
            ruta.paradas.set(paradas[i - 1:i + 2])
            rutas.append(ruta)

        # Vehículos
        for i in range(1, 6):
            Vehiculo.objects.get_or_create(
                placa=f'ABC-10{i}',
                defaults={
                    'tipo': Vehiculo.Tipo.BUS if i % 2 else Vehiculo.Tipo.METRO,
                    'capacidad': 40,
                    'activo': True,
                    'ruta': rutas[i - 1],
                    'conductor': conductores[i - 1],
                    'creado_por': administrador,
                })

        self.stdout.write(self.style.SUCCESS('Datos de prueba cargados.'))