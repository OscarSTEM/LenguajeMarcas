from lxml import etree

#Cargar el archivo XML
tree = etree.parse("circuits.xml")
root = tree.getroot()