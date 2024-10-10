import xml.etree.ElementTree as xml
import os, json
"""
Ejercicio
"""

data = { # Diccionario de datos
    "name" : "Marco Polo",
    "age" : 39,
    "birth_date" : "29-03-1998",
    "programming_languages" : ["Python", "C++", "Java"]
}

xml_file = "ipfabio.xml"
json_file = "ipfabio.json"

# XML

def create_xml():
    root =xml.Element("data") # Raíz

    for key, value in data.items(): # Recorremos el diccionario separando "Clave": "Valor".
        child = xml.SubElement(root, key) # Asignamos root como elemento raiz, y "Clave" como nombre de etiqueta.
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, "item").text = item
        else:
            child.text = str(value) # Le asignamos el "Value" del diccionario al subelemento.

    tree = xml.ElementTree(root)
    tree.write(xml_file)

create_xml()

with open(xml_file, "r") as xml_data:
    print(xml_data.read())

# Borrar
if os.path.exists(xml_file):
    os.remove(xml_file)

# Json

def create_json():

    with open(json_file, "w") as json_data:
        json.dump(data, json_data)

create_json()

with open(json_file, "r") as json_data:
    print(json_data.read())

# Borrar
if os.path.exists(json_file):
    os.remove(json_file)

"""
Extra
"""

create_xml()
create_json()

class Data:

    def __init__(self, name, age, birth_date, programming_languages) -> None:
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.programming_languages = programming_languages

with open(xml_file, "r") as xml_data:

    root = xml.fromstring(xml_data.read())
    name = root.find("name").text
    age = root.find("age").text
    birth_date = root.find("birth_date").text
    programming_languages = []
    for item in root.find("programming_languages"):
        programming_languages.append(item.text)

    data_from_xml = Data(name, age, birth_date, programming_languages)
    print(data_from_xml.__dict__)

with open(json_file, "r") as json_data:
    json_dict = json.load(json_data)
    json_class = Data(name = json_dict["name"], age = json_dict["age"], birth_date = json_dict["birth_date"], programming_languages = json_dict["programming_languages"])
    print(json_class.__dict__)


# Borrar XMl
if os.path.exists(xml_file):
    os.remove(xml_file)


# Borrar Json
if os.path.exists(json_file):
    os.remove(json_file)