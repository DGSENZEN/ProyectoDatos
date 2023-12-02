# Prueba de Desempeño 🖥️ Modelado de Datos


PD3 de Modelado de Datos
Equipo: Alberto Baeza, Luis Palma, Diego Gaytan

1. Identificar un	dataset	de	kaggle	(https://www.kaggle.com/datasets)	que	pueda	
ser	modelado	con	su	BD	NoSQL (que	no	se	haya	utilizado	durante	el	curso).
2. Haciendo	uso	de	un	repositorio	de	Github,	documente	lo	siguiente:
   * Agregar el	archivo	del	dataset
   * Descripción	del	dataset
   * Descripción	del	diccionario	de	datos	del	dataset
   * Descripción	del	modelado	del	dataset	según	la	BD	NoSQL
   * Descripción	de	la	BD	NoSQL	y	las	herramientas	que	se	utilizaron.
   * Descripción	de	la	importación	de	sus	datos.
 <br> Para la importación del dataset se tuvo que realizar una modificación de la extensión .csv a .json, esto se debe a que CouchDB solo reconoce este tipo de extensión. En este cambio se utilizo un script en python llamado 'convertidor.py', el cual identifica el tipo de la codificación que tiene el csv para posteriormente hacer la conversion a json.
<br>  Luego, ya con la extensión correcta se utilizo el script 'subirDataSet.py', con ese documento se sube el dataset a la BD, utilizando como recurso la API que tiene CouchDB.
   * Definir	 y	 describir	 al	 menos	 5	 sentencias	 para	 cada	 una	 de	 las	
    operaciones	CRUD (Create,	Read,	Update,	Delete) en	la	BD.	
3. El	 github deberá	 estar	 organizado	 de	 tal	 manera	 que	 sea	 fácil	 navegar	 o	
identificar	los	puntos	antes	mencionados.
4. En	la	plataforma	Moodle	subir	la	URL	del	repositorio.
5. Deberán	presentar	el	trabajo	realizado	a	sus	compañeros	en	el	salón	de	clases	
(verificar	tabla	de cotejo).



