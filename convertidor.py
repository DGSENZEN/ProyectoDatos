import pandas as pd   #libreria para poder abrir el csv
import chardet        #libreria para poder reconocer la codificación del csv

""" Esta parte nos sirve para poder reconocer el tipo de codificación que tiene el csv, ya que, para poder leer el documento con pandas
es necesario conocer la codificación para hacer la conversion posteriormente"""

with open('albumlist.csv', 'rb') as f:
    result = chardet.detect(f.read())


# Leer el archivo CSV
data = pd.read_csv('albumlist.csv', encoding=result['encoding'])

# Convertir a JSON 
#cada fila del dataset se convertirá en un objeto json individual
json_data = data.to_json(orient='records')

print(json_data)

#se crea el archivo con extension json
with open('dataset.json', 'w') as f:
    f.write(json_data)
