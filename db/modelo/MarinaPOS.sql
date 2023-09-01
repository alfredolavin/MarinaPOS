PRAGMA writable_schema = 1;
delete from sqlite_master where type in ('view', 'table', 'index', 'trigger');
PRAGMA writable_schema = 0;

CREATE TABLE producto(
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  unidad_de_concentracion_id INTEGER NOT NULL,
  cantidad INTEGER,
  concentracion TEXT,
  laboratorio_id INTEGER NOT NULL,
  forma_farmaceutica_id INTEGER NOT NULL,
  nombre TEXT NOT NULL,
  precio INTEGER NOT NULL,
  costo INTEGER NOT NULL,
  stock INTEGER,
  principio_activo TEXT,
  registro_isp TEXT,
  es_generico BOOLEAN,
  es_bioequivalente BOOLEAN,
  es_refrigerado BOOLEAN,
  es_controlado BOOLEAN,
  es_activo BOOLEAN,
  es_petitorio_minimo BOOLEAN,
  CONSTRAINT laboratorio_producto FOREIGN KEY (laboratorio_id) REFERENCES laboratorio (id),
  CONSTRAINT forma_farmaceutica_producto FOREIGN KEY (forma_farmaceutica_id) REFERENCES forma_farmaceutica (id),
  CONSTRAINT unidad_de_medida_producto FOREIGN KEY (unidad_de_concentracion_id) REFERENCES unidad_de_medida (id)
);

  CREATE INDEX productos_ix_1 ON producto(nombre);
  
  CREATE INDEX producto_ix_2 ON producto(principio_activo);
  
CREATE TABLE codigo_de_barras(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  barras TEXT NOT NULL,
  producto_id INTEGER NOT NULL,
  CONSTRAINT productos_codigos_de_barra FOREIGN KEY (producto_id) REFERENCES producto (id)
);

  CREATE UNIQUE INDEX codigo_de_barras_ix_1 ON codigo_de_barras(barras);
  
CREATE TABLE documento(
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  turno_id INTEGER NOT NULL,
  tipo_documento_id INTEGER NOT NULL,
  estado_documento_id INTEGER NOT NULL,
  momento DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  total_documento INTEGER NOT NULL,
  comentario TEXT,
  CONSTRAINT tipo_documento_documento FOREIGN KEY (tipo_documento_id) REFERENCES tipo_documento (id),
  CONSTRAINT estado_documento_documento FOREIGN KEY (estado_documento_id) REFERENCES estado_documento (id),
  CONSTRAINT turno_documento FOREIGN KEY (turno_id) REFERENCES turno (id)
);

  CREATE INDEX documentos_ix_1 ON documento(momento);
  
CREATE TABLE usuario(
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  nombre TEXT NOT NULL,
  rut TEXT NOT NULL,
  apodo TEXT NOT NULL
);

CREATE TABLE tipo_documento(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nombre TEXT);

  CREATE UNIQUE INDEX tipo_documento_ix_1 ON tipo_documento(nombre);
  
CREATE TABLE estado_documento(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nombre TEXT);

  CREATE UNIQUE INDEX estado_documento_ix_1 ON estado_documento(nombre);
  
CREATE TABLE forma_farmaceutica(
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  nombre TEXT,
  unidad_de_medida_id INTEGER NOT NULL,
  CONSTRAINT unidad_de_medida_forma_farmaceutica FOREIGN KEY (unidad_de_medida_id) REFERENCES unidad_de_medida (id)
);

  CREATE UNIQUE INDEX forma_farmaceutica_ix_1 ON forma_farmaceutica(nombre);
  
CREATE TABLE unidad_de_medida(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nombre TEXT);

  CREATE UNIQUE INDEX unidad_de_medida_ix_1 ON unidad_de_medida(nombre);
  
CREATE TABLE laboratorio(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nombre TEXT);

  CREATE UNIQUE INDEX laboratorio_ix_1 ON laboratorio(nombre);
  
CREATE TABLE turno(
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  usuario_id INTEGER NOT NULL,
  primer_movimiento DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  monto_caja_inicial INTEGER NOT NULL,
  ultimo_movimiento DATETIME,
  monto_caja_final INTEGER,
  monto_caja_final_real INTEGER,
  comentario TEXT,
  CONSTRAINT usuario_turno FOREIGN KEY (usuario_id) REFERENCES usuario (id)
);

CREATE TABLE movimiento(
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  documento_id INTEGER NOT NULL,
  producto_id INTEGER NOT NULL,
  estado_movimiento_id INTEGER NOT NULL,
  producto_nombre TEXT NOT NULL,
  producto_precio INTEGER NOT NULL,
  producto_costo INTEGER NOT NULL,
  precio_cobrado INTEGER NOT NULL,
  multiplicador INTEGER NOT NULL,
  CONSTRAINT producto_movimiento FOREIGN KEY (producto_id) REFERENCES producto (id),
  CONSTRAINT documento_movimiento FOREIGN KEY (documento_id) REFERENCES documento (id),
  CONSTRAINT estado_movimiento_movimiento FOREIGN KEY (estado_movimiento_id) REFERENCES estado_movimiento (id)
);

CREATE TABLE estado_movimiento(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nombre TEXT);

  CREATE UNIQUE INDEX estado_movimiento_ix_1 ON estado_movimiento(nombre);
  