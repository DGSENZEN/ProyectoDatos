# Prueba de Desempeño 🖥️ Modelado de Datos


### Prueba de Desempeño 3 - Implementación de Dataset con noSQL <br>
### Equipo _02_: 
* Alberto Enrique Baeza Vivas 🦧
* Luis Manuel Palma Pinto 🦖
* Diego Gaytan Bolaños 🐳

1. Identificar un	dataset	de	kaggle	(https://www.kaggle.com/datasets)	que	pueda	ser	modelado	con	su	BD	NoSQL (que	no	se	haya	utilizado	durante	el	curso)<br> Dataset utilizado : https://www.kaggle.com/datasets/notgibs/500-greatest-albums-of-all-time-rolling-stone. 🔍
2. Haciendo	uso	de	un	repositorio	de	Github,	documente	lo	siguiente: 📝
   * **a.** Agregar el	archivo	del	dataset
<br> > El archivo del dataset se llama "_albums.csv_", al estar en formato **csv** para que este funcione utilizamos un programa que hicimos en **python** para convertirlo a formato **JSON** y que funcionara en el **CouchDB**, este programa se llama "_convertidor.py_", más información en su punto respectivo.
   * **b.** Descripción	del	dataset
<br> > El dataset muestra el top 500 de los albumes mejor valorados, de acuerdo con la revista Rolling Stone, este dataset muestra el puesto, nombre, año, artista, genero y subgenero de cada album en la lista.
   * **c.** Descripción	del	diccionario	de	datos	del	dataset
<br> > Usando un script de Python, se filtro la informacion y se creo un diccionario de datos en buen formato y organizado con su respectiva informacion y datos necesarios. El archivo **dictdatos.py** es el que nos ayuda a obtener el diccionario de datos, mientras que el diccionario en si es **output_data.json** ambos se encuentran en el repositorio.
   * **d.** Descripción	del	modelado	del	dataset	según	la	BD	NoSQL
  <br> > Nuestra base de datos tiene documentos en los que almacena una representación de un álbum de música. Esta representación viene a estar dada por documentos **JSON** los cuales son representativos a un modelo **Clave-Valor**. Por otro lado, cada uno de estos documentos almacena la siguiente información: Number, Year, Album, Artist, Genre, y Subgenre.
   * **e.** Descripción	de	la	BD	NoSQL	y	las	herramientas	que	se	utilizaron.
   <br> > La base de datos utilizada es **CouchDB** la cual es una base de datos orientada a documentos, que se comunica a través de ua API HTTP y almacena datos en formato **JSON**.
<br> Por otro lado, se utilizaron herramientas externas como **Python** junto con la instalación de algunas librerías tales como **Pandas**, **CouchDB**, **JSON**, **Chardet** las cuales fueron utiles para realizar la importación del dataset. Todo este proceso fue realizado utilizando **VSCode**. Tambien se utilizo la interfaz web **Fauxton** para poder crear la DB y poder visualizar los datos.
<br> **Nota:** Se utilizo esta base de datos en lugar de DynamoDB debido a que había que pagar por su uso.

   * **f.** Descripción	de	la	importación	de	sus	datos.
##### Antes de importar 
<br> > Antes de realizar la importación de los datos primero se tuvo que haber creado la BD, nosotros realizamos este paso de manera manual directo desde el cliente de CouchDB. Para ello, con el CouchDB instalado nos dirigimos a nuestro navegador y utilizamos la siguiente liga: [local](http://localhost:5984/_utils/#login)
<br> Posteriormente de haber ingresado nuestro usuario y contraseña, simplemente le damos clic a la parte superior derecha del cliente donde dice 'Create Database' 
<br> ![image](https://github.com/DGSENZEN/ProyectoDatos/assets/148842609/3d77a5dd-e6fc-427f-86ba-9dab3f3bd6d4)
<br> En nuestro caso, decidimos utilizar el nombre de 'albums' y creamos. 
<br> ![image](https://github.com/DGSENZEN/ProyectoDatos/assets/148842609/526dd51f-fa3a-43a3-9480-9205f7a4dc16)
<br>Nos daremos cuenta que fue creada con éxito si aparece así:
![image](https://github.com/DGSENZEN/ProyectoDatos/assets/148842609/8268a9f8-7498-4dcd-9286-01dfb80c0e60)
##### Ahora, sí. Para importar
<br> > Para la importación del dataset se tuvo que realizar una modificación de la extensión .csv a .json, esto se debe a que CouchDB solo reconoce este tipo de extensión. En este cambio se utilizo un script en python llamado **'convertidor.py'**, el cual identifica el tipo de la codificación que tiene el csv para posteriormente hacer la conversion a json.
<br> > Luego, ya con la extensión correcta se utilizo el script **'subirDataSet.py'**, con ese documento se sube el dataset a la BD, utilizando como recurso la API que tiene CouchDB. Podemos darnos cuenta que efectivamete si se realizo bien la importación ya que contiene los 500 elementos que esperabamos. 
<br>
<br> **Nota** : Dentro de cada uno de los scripts hay una descripción más detallada de cómo funciona.
<br>
![image](https://github.com/DGSENZEN/ProyectoDatos/assets/148842609/398f48e6-55b2-4864-8e2f-4276ae6aba53)
<br>
<br>Veamos una parte de los datos que se importaron
<br>![image](https://github.com/DGSENZEN/ProyectoDatos/assets/148842609/3a387cbd-d786-42e7-be9e-da8605696179)

   * **g.** Definir	 y	 describir	 al	 menos	 5	 sentencias	 para	 cada	 una	 de	 las operaciones	CRUD (Create,	Read,	Update,	Delete) en	la	BD.
<br> **IMPORTANTE**: En los codigos se usa admin:admin como un nombre predeterminado para el usuario y su contraseña, para modificarlo tendria que cambiarlo al que tiene en uso en su CouchDB.
<br> En CouchDB las operaciones CRUD se realizan usando metodos **HTTP** en los documentos de la base de datos. 
<br> > **Create** (Aqui se conocen como comandos "**POST**")
<br> >> Crear un nuevo documento con datos especificos: curl -u admin:admin -X POST http://localhost:5984/albums -H "Content-Type: application/json" -d '{"number": 501, "year": 2010, "album": "Razor", "artist": "The Colds", "genre:" "Rock", "subgenre:" "Pop rock"}'
<br> >> Agregar un nuevo documento con atributos unicos: curl -u admin:admin -X POST http://localhost:5984/albums -H "Content-Type: application/json" -d '{"titulo": "Rock y más", "contenido": "Descubre la historia del rock."}'
<br> >> Insertar un documento con un arreglo: curl -u admin:admin -X POST http://localhost:5984/albums -H "Content-Type: application/json" -d '{"generos": ["rock", "pop", "hip hop"]}'
<br> >> Crear un documento con objetos anidados: curl -u admin:admin -X POST http://localhost:5984/albums -H "Content-Type: application/json" -d '{"artista": {"nombre": "Bob", "apellido": "dylan"}}'
<br> >> Insertar un documento con campo booleano: curl -u admin:admin -X POST http://localhost:5984/albums -H "Content-Type: application/json" -d '{"activo": true}'
<br> > **Read** (Aqui se conocen como comandos "**GET**")
<br> >> Obtener un documento especifico por su id: curl -u admin:admin -X GET http://localhost:5984/albums/id_deldocumento
<br> >> Obtener todos los documentos de la base de datos: curl -u admin:admin -X GET http://localhost:5984/albums/_all_docs
<br> >> Obtener documentos con caracteres/referencias especificas: curl -u admin:admin -X GET http://localhost:5984/albums/_design/example/_view/by_year?startkey=1950&endkey=2000 Obtiene los albumes entre los años 50s y los 2000es
<br> >> Obtener documentos con un valor particular: curl -u admin:admin -X GET http://localhost:5984/albums/_design/example/_view/by_artist?key="The Beatles"
<br> >> Obtener documentos con booleanos que sean verdad: curl -u admin:admin -X GET http://localhost:5984/albums/_design/example/_view/activo?key=true
<br> > **Update** (Aqui se llaman comandos "**PUT**" / "**PATCH**")
<br> >> Actualizar un documento: curl -u admin:admin -X PUT http://localhost:5984/albums/id_deldocumento -H "Content-Type: application/json" -d '{"number": 499, "year": 2015, "album": "Bash", "artist": "The Colds", "genre:" "Rock", "subgenre:" "Soul rock"}'
<br> >> Modificar un atributo especifico de un documento: curl -u admin:admin -X PATCH http://localhost:5984/albums/id_deldocumento -H "Content-Type: application/json" -d '{"year": 32}'
<br> >> Agregar un nuevo atributo a un documento: curl -u admin:admin -X PUT http://localhost:5984/albums/id_deldocumento -H "Content-Type: application/json" -d '{"disquera": "Sharp Records"}'
<br> >> Actualizar objetos anidados: curl -u admin:admin -X PATCH http://localhost:5984/albums/id_deldocumento -H "Content-Type: application/json" -d '{"artista": {"Apellido": "Hendrix"}}'
<br> >> Actualizar el arreglo de un documento: curl -u admin:admin -X PATCH http://localhost:5984/albums/id_deldocumento -H "Content-Type: application/json" -d '{"generos": ["rock, nu rock, metal"]}'
<br> > **Delete**
<br> >> Borrar un documento especifico por su id: curl -u admin:admin -X DELETE http://localhost:5984/albums/id_deldocumento
<br> >> Borrar una base de datos: curl -u admin:admin -X DELETE http://localhost:5984/albums
<br> >> Borrar un atributo especifico del documento (Usando **PATCH**): curl -u admin:admin -X PATCH http://localhost:5984/albums/id_deldocumento -H "Content-Type: application/json" -d '{"subgenero": null}'
<br> >> Borrar attachments del documento: curl -u admin:admin -X DELETE http://localhost:5984/albums/id_deldocumento/nombredel_attachment
<br> >> Purgar un documento (Se borrara permanentemente): curl -u admin:admin -X POST http://localhost:5984/albums/_purge -H "Content-Type: application/json" -d '{"id_deldocumento": {"rev": "document_revision"}}'
<br> 3. El	 github deberá	 estar	 organizado	 de	 tal	 manera	 que	 sea	 fácil	 navegar	 o identificar	los	puntos	antes	mencionados. 🧭
<br> 4. En	la	plataforma	Moodle	subir	la	URL	del	repositorio. ⬆️
<br> 5. Deberán	presentar	el	trabajo	realizado	a	sus	compañeros	en	el	salón	de	clases	(verificar	tabla	de cotejo). 🎥
