import couchdb
import json
""" 
En caso de no tener las librerias utilizar las siguientes instalaciones: 
pip install CouchDB
pip install json
"""


# Conectar al servidor CouchDB
#para ello se utiliza la direccion del servidor junto con el usuario y contraseña
#http://usuario:contraseña
couch = couchdb.Server('http://admin:admin@localhost:5984/')

# Se debe poner el nombre de la BD que se creo en el cliente
db = couch['albums']

# Leemo el archivo Json
with open('dataset.json', 'r') as f:
    data = json.load(f)

# Se guarda cada uno de los documentos en la BD
for doc in data:
    db.save(doc)
