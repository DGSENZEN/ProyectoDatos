# Prueba de Desempeño 🖥️ Modelado de Datos


### Prueba de Desempeño 3 - Implementación de Dataset con noSQL <br>
### Equipo _02_: 
* Alberto Enrique Baeza Vivas 🦧
* Luis Manuel Palma Pinto 🦖
* Diego Gaytan Bolaños 🐳

1. Identificar un	dataset	de	kaggle	(https://www.kaggle.com/datasets)	que	pueda	ser	modelado	con	su	BD	NoSQL (que	no	se	haya	utilizado	durante	el	curso). 🔍
2. Haciendo	uso	de	un	repositorio	de	Github,	documente	lo	siguiente: 📝
   * Agregar el	archivo	del	dataset
<br> > El archivo del dataset se llama "_albums.csv_", al estar en formato **csv** para que este funcione utilizamos un programa que hicimos en **python** para convertirlo a formato **JSON** y que funcionara en el **CouchDB**, este programa se llama "_convertidor.py_", más información en su punto respectivo.
   * Descripción	del	dataset
<br> > El dataset muestra el top 500 de los albumes mejor valorados, de acuerdo con la revista Rolling Stone, este dataset muestra el puesto, nombre, año, artista, genero y subgenero de cada album en la lista.
   * Descripción	del	diccionario	de	datos	del	dataset
   * Descripción	del	modelado	del	dataset	según	la	BD	NoSQL
   * Descripción	de	la	BD	NoSQL	y	las	herramientas	que	se	utilizaron.
   * Descripción	de	la	importación	de	sus	datos.
##### Antes de importar 
<br> > Antes de realizar la importación de los datos primero se tuvo que haber creado la BD, nosotros realizamos este paso de manera manual directo desde el cliente de CouchDB. Para ello, con el CouchDB instalado nos dirigimos a nuestro navegador y utilizamos la siguiente liga: [local](http://localhost:5984/_utils/#login)
<br> Posteriormente de haber ingresado nuestro usuario y contraseña, simplemente le damos clic a la parte superior derecha del cliente donde dice 'Create Database' 
<br> ![image](https://github.com/DGSENZEN/ProyectoDatos/assets/148842609/3d77a5dd-e6fc-427f-86ba-9dab3f3bd6d4)
<br> En nuestro caso, decidimos utilizar el nombre de 'albums' y creamos. 
<br> ![image](https://github.com/DGSENZEN/ProyectoDatos/assets/148842609/526dd51f-fa3a-43a3-9480-9205f7a4dc16)
<br>Nos daremos cuenta que fue creada con éxito si aparece así:
![image](https://github.com/DGSENZEN/ProyectoDatos/assets/148842609/8268a9f8-7498-4dcd-9286-01dfb80c0e60)
##### Ahora, sí. Para importar
<br> > Para la importación del dataset se tuvo que realizar una modificación de la extensión .csv a .json, esto se debe a que CouchDB solo reconoce este tipo de extensión. En este cambio se utilizo un script en python llamado 'convertidor.py', el cual identifica el tipo de la codificación que tiene el csv para posteriormente hacer la conversion a json.
<br> > Luego, ya con la extensión correcta se utilizo el script 'subirDataSet.py', con ese documento se sube el dataset a la BD, utilizando como recurso la API que tiene CouchDB. Podemos darnos cuenta que efectivamete si se realizo bien la importación ya que contiene los 500 elementos que esperabamos. 
![image](https://github.com/DGSENZEN/ProyectoDatos/assets/148842609/398f48e6-55b2-4864-8e2f-4276ae6aba53)
<br>
<br>Veamos una parte de los datos que se importaron
<br>![image](https://github.com/DGSENZEN/ProyectoDatos/assets/148842609/3a387cbd-d786-42e7-be9e-da8605696179)



   * Definir	 y	 describir	 al	 menos	 5	 sentencias	 para	 cada	 una	 de	 las operaciones	CRUD (Create,	Read,	Update,	Delete) en	la	BD.	
3. El	 github deberá	 estar	 organizado	 de	 tal	 manera	 que	 sea	 fácil	 navegar	 o identificar	los	puntos	antes	mencionados. 🧭
4. En	la	plataforma	Moodle	subir	la	URL	del	repositorio. ⬆️
5. Deberán	presentar	el	trabajo	realizado	a	sus	compañeros	en	el	salón	de	clases	(verificar	tabla	de cotejo). 🎥
