from lxml import etree

#Cargar el archivo XML
drivers = etree.parse("drivers.xml")
rootDrivers = drivers.getroot()

circuits = etree.parse("circuits.xml")
rootCircuits = circuits.getroot()
#1º Reciba por teclado el nombre de un país y una nacionalidad y 
# muestre la lista de pilotos y de circuitos de dicho país y 
# nacionalidad (dos listas).


piloto1 = input("Introduce el pais: ")
pais = drivers.xpath(f"driver[nationality ='{piloto1}']/driverRef/text()")
print(pais)

piloto2 = input("Introduce la nacionalidad: ")
nacionalidad = circuits.xpath(f"circuit[country ='{piloto2}']/circuitRef/text()")
print(nacionalidad)

#2º Muestre el circuito a mayor altitud (alt).
maxAlt = int(input("¿Introduzca una Alt?: "))
print(circuits.xpath(f"circuit/alt/text()"))
# 3º Reciba por teclado una altitud (alt) e indique cuántos circuitos están 
# por encima de dicha altitud y cuántos por debajo.
altitud = ("Introduce una altitud: ")
print(circuits.xpath(f"circuit['alt > and circuit={altitud}' ]/circuitRef/text()"))