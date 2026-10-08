# Condicional if
# simple

combustible = 5
if combustible >= 10:
    print("Puedes despegar")
    
# Condicional if-else

creditos = int(input("Ingrese la cantidad de créditos que tiene: "))
precio_repuesto = int(input("Ingrese el precio del repuesto: "))
if creditos >= precio_repuesto:
    print("Puedes comprar el repuesto")
else:
    print("No tienes suficiente crédito para comprar el repuesto")
    
# if anidado

if creditos >= precio_repuesto:
    print("Puedes comprar el repuesto")
    if creditos > precio_repuesto:
        print("Te sobran créditos")
    else:
        print("Te quedas justo con los créditos necesarios")
else:
    print("No tienes suficiente crédito para comprar el repuesto")
    
# Condicional if-elif-else

if creditos >= precio_repuesto:
    print("Puedes comprar el repuesto y te sobran créditos")
elif creditos == precio_repuesto:
    print("Puedes comprar el repuesto y te quedas justo con los créditos necesarios")
else:
    print("No tienes suficiente crédito para comprar el repuesto")
    
tipo_respuesto = input("Ingrese el tipo de repuesto que desea comprar (Motor, Ala o Escudo): ")
if tipo_respuesto == "Motor" and creditos >= precio_repuesto and tipo_respuesto == "Ala":
    print("Puedes comprar el repuesto y te sobran créditos")
elif tipo_respuesto == "Ala" and creditos >= precio_repuesto:
    print("Puedes comprar el repuesto y te sobran créditos")
elif tipo_respuesto == "Escudo" and creditos >= precio_repuesto:
    print("Puedes comprar el repuesto y te sobran créditos")
else:
    print("Tipo de repuesto no valido")

print("-" * 50)
print("Ejercicio en clase")
peso_paquete = float(input("Ingrese el peso del paquete en Kilogramos: "))
zona_destino = int(input("Ingrese la zona de destino (1 = America), (2 = Europa), (3 = Resto del mundo): "))
if zona_destino == 1:
    precio_total = peso_paquete * 5.0
    print("-" * 50)
    print("El precio total del envío es:", precio_total,"$ y sera enviado a America")
    print("-" * 50)
elif zona_destino == 2:
    precio_total = peso_paquete * 7.5
    print("-" * 50)
    print("El precio total del envío es:", precio_total,"$ y sera enviado a Europa")
    print("-" * 50)
elif zona_destino == 3:
    precio_total = peso_paquete * 10.0
    print("-" * 50)
    print("El precio total del envío es:", precio_total,"$ y sera enviado al Resto del mundo")
    print("-" * 50)
else:
    print("-" * 50)
    print("Zona de destino no valida")
    print("-" * 50)