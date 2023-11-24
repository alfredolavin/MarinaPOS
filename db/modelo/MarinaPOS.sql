PRAGMA writable_schema = 1;
delete from sqlite_master where type in ('view', 'table', 'index', 'trigger');
PRAGMA writable_schema = 0;

CREATE TABLE producto(
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  nombre TEXT NOT NULL,
  cantidad INTEGER NOT NULL,
  forma_farmaceutica_id INTEGER NOT NULL,
  laboratorio_id INTEGER NOT NULL,
  es_generico BOOLEAN,
  es_bioequivalente BOOLEAN,
  es_refrigerado BOOLEAN,
  es_controlado BOOLEAN,
  es_desactivado BOOLEAN,
  es_cenabast BOOLEAN,
  CONSTRAINT laboratorio_producto FOREIGN KEY (laboratorio_id) REFERENCES laboratorio (id),
  CONSTRAINT forma_farmaceutica_producto FOREIGN KEY (forma_farmaceutica_id) REFERENCES forma_farmaceutica (id)
);

  CREATE INDEX productos_ix_1 ON producto;
  
CREATE TABLE codigo_de_barras(
  id TEXT NOT NULL,
  producto_id INTEGER NOT NULL,
  tipo_detalle_id INTEGER NOT NULL,
  detalle TEXT,
  PRIMARY KEY(id),
  CONSTRAINT productos_codigos_de_barra FOREIGN KEY (producto_id) REFERENCES producto (id),
  CONSTRAINT tipo_detalle_codigo_de_barras FOREIGN KEY (tipo_detalle_id) REFERENCES tipo_detalle (id)
);

  CREATE UNIQUE INDEX codigo_de_barras_ix_1 ON codigo_de_barras(id);
  
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
  CONSTRAINT unidad_de_medida_forma_farmaceutica
    FOREIGN KEY (unidad_de_medida_id) REFERENCES unidad_de_medida (unidad_de_medida_id)
);

  CREATE UNIQUE INDEX forma_farmaceutica_ix_1 ON forma_farmaceutica(nombre);
  
CREATE TABLE unidad_de_medida
  (unidad_de_medida_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nombre TEXT NOT NULL, descripcion TEXT NOT NULL);

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
  
CREATE TABLE codigo_atc(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nombre TEXT NOT NULL, descripcion TEXT NOT NULL);

CREATE TABLE principio_activo(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nombre TEXT NOT NULL);

CREATE TABLE principio_activo_y_producto(
  producto_id INTEGER NOT NULL,
  principio_activo_id INTEGER NOT NULL,
  PRIMARY KEY(producto_id, principio_activo_id),
  CONSTRAINT producto_table1 FOREIGN KEY (producto_id) REFERENCES producto (id),
  CONSTRAINT principio_activo_table1 FOREIGN KEY (principio_activo_id) REFERENCES principio_activo (id)
);

CREATE TABLE tipo_detalle(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nombre_detalle TEXT NOT NULL);

CREATE TABLE producto_precio(
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  producto_id INTEGER NOT NULL,
  momento DATETIME NOT NULL,
  precio_venta INTEGER NOT NULL,
  precio_compra INTEGER,
  turno_id INTEGER NOT NULL,
  CONSTRAINT producto_producto_precio FOREIGN KEY (producto_id) REFERENCES producto (id),
  CONSTRAINT turno_producto_precio FOREIGN KEY (turno_id) REFERENCES turno (id)
);

CREATE TABLE principio_activo_y_codigo_atc(
  codigo_atc_id INTEGER NOT NULL,
  principio_activo_id INTEGER NOT NULL,
  PRIMARY KEY(codigo_atc_id, principio_activo_id),
  CONSTRAINT principio_activo_principio_activo_y_codigo_atc
    FOREIGN KEY (principio_activo_id) REFERENCES principio_activo (id),
  CONSTRAINT codigo_atc_principio_activo_y_codigo_atc FOREIGN KEY (codigo_atc_id) REFERENCES codigo_atc (id)
);

CREATE TABLE detalles_farmaceuticos(
  id INTEGER NOT NULL,
  cenabast❓ BOOLEAN,
  controlado❓ BOOLEAN,
  refrigerado❓ BOOLEAN,
  bioequivalente❓ BOOLEAN,
  generico❓ BOOLEAN,
  PRIMARY KEY(id),
  CONSTRAINT producto_detalles_farmaceuticos FOREIGN KEY (id) REFERENCES producto (id)
);
