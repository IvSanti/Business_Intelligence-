CREATE TABLE pelicula (
	id_pelicula integer PRIMARY KEY,
	nombre_pelicula varchar(100),
	fecha_lanzamiento date,
	popularidad integer,
	sinopsis varchar(500),
	origen varchar(100),
	api varchar(100),
	cloudWatch varchar(100),
	fecha_consulta timestamp,
	fecha_carga timestamp
);

CREATE TABLE credito(
	id_credito integer PRIMARY KEY,
	nombre_persona varchar(50),
	departamento varchar(50),
	personaje_oficio varchar(50),
	origen varchar(200),
	api varchar(100),
	cloudWatch varchar(100),
	fecha_consulta timestamp,
	fecha_carga timestamp
);

CREATE TABLE detalle(
	id_detail integer PRIMARY KEY,
	web varchar(200),
	lenguje_original varchar(10),
	productora varchar (50),
	origen varchar(200),
	api varchar(100),
	cloudWatch varchar(100),
	fecha_consulta timestamp,
	fecha_carga timestamp
);