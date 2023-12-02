import couchdb
import json

# Conectar al servidor CouchDB
#http://usuario:contraseña
couch = couchdb.Server('http://admin:admin@localhost:5984/')

# Seleccionar la base de datos
db = couch['albums']

# Leer el archivo JSON
with open('dataset.json', 'r') as f:
    data = json.load(f)

# Guardar cada documento en la base de datos
for doc in data:
    db.save(doc)
