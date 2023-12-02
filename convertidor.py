import pandas as pd
import chardet

#esta parte sirve para poder detectar el tipo de codificacion que tiene el archivo csv
with open('albumlist.csv', 'rb') as f:
    result = chardet.detect(f.read())


# Leer el archivo CSV
data = pd.read_csv('albumlist.csv', encoding=result['encoding'])
# Convertir a JSON
json_data = data.to_json(orient='records')

print(json_data)

with open('dataset.json', 'w') as f:
    f.write(json_data)
