PRAGMA writable_schema = 1;

delete from sqlite_master
where
  type in ('view', 'table', 'index', 'trigger');

PRAGMA writable_schema = 0;

CREATE TABLE
  producto (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    pharmid TEXT,
    nombre TEXT NOT NULL,
    laboratorio_id INTEGER,
    categoria_farmacologica_id INTEGER,
    forma_farmaceutica_id INTEGER,
    principio_activo_id INTEGER,
    tipo_receta_id INTEGER,
    registro_isp TEXT,
    es_cenabast BOOLEAN,
    es_controlado BOOLEAN,
    es_refrigerado BOOLEAN,
    es_bioequivalente BOOLEAN,
    es_generico BOOLEAN,
    cantidad_por_envase INTEGER,
    CONSTRAINT laboratorio_producto FOREIGN KEY (laboratorio_id) REFERENCES laboratorio (id),
    CONSTRAINT id_producto FOREIGN KEY (categoria_farmacologica_id) REFERENCES categoria_farmacologica (id),
    CONSTRAINT forma_farmaceutica_producto FOREIGN KEY (forma_farmaceutica_id) REFERENCES forma_farmaceutica (id),
    CONSTRAINT tipo_receta_producto FOREIGN KEY (tipo_receta_id) REFERENCES tipo_receta (id),
    CONSTRAINT principio_activo_producto FOREIGN KEY (principio_activo_id) REFERENCES principio_activo (id)
  );

CREATE TABLE
  codigo_de_barras (
    id TEXT NOT NULL,
    producto_id INTEGER NOT NULL,
    detalle_codigo_barras_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT productos_codigos_de_barra FOREIGN KEY (producto_id) REFERENCES producto (id),
    CONSTRAINT detalle_codigo_barras_codigo_de_barras FOREIGN KEY (detalle_codigo_barras_id) REFERENCES detalle_codigo_barras (id)
  );

CREATE UNIQUE INDEX codigo_de_barras_ix_1 ON codigo_de_barras (id);

CREATE TABLE
  documento (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    tipo_documento_id INTEGER NOT NULL,
    estado_documento_id INTEGER NOT NULL,
    cliente_id INTEGER NOT NULL,
    momento DATETIME NOT NULL DEFAULT (datetime ('now', 'localtime')),
    total_documento INTEGER NOT NULL,
    comentario TEXT,
    turno_id INTEGER NOT NULL,
    CONSTRAINT tipo_documento_documento FOREIGN KEY (tipo_documento_id) REFERENCES tipo_documento (id),
    CONSTRAINT estado_documento_documento FOREIGN KEY (estado_documento_id) REFERENCES estado_documento (id),
    CONSTRAINT turno_documento FOREIGN KEY (turno_id) REFERENCES turno (id),
    CONSTRAINT cliente_documento FOREIGN KEY (cliente_id) REFERENCES cliente (id)
  );

CREATE INDEX documentos_ix_1 ON documento (momento);

CREATE TABLE
  usuario (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre TEXT NOT NULL,
    rut TEXT NOT NULL,
    apodo TEXT NOT NULL
  );

CREATE TABLE
  tipo_documento (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre TEXT
  );

CREATE UNIQUE INDEX tipo_documento_ix_1 ON tipo_documento (nombre);

CREATE TABLE
  estado_documento (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre TEXT
  );

CREATE UNIQUE INDEX estado_documento_ix_1 ON estado_documento (nombre);

CREATE TABLE
  forma_farmaceutica (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre TEXT,
    unidad_de_medida_id INTEGER NOT NULL,
    CONSTRAINT unidad_de_medida_forma_farmaceutica FOREIGN KEY (unidad_de_medida_id) REFERENCES unidad_medida (id)
  );

CREATE UNIQUE INDEX forma_farmaceutica_ix_1 ON forma_farmaceutica (nombre);

CREATE TABLE
  unidad_medida (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre TEXT NOT NULL
  );

CREATE UNIQUE INDEX unidad_de_medida_ix_1 ON unidad_medida (nombre);

CREATE TABLE
  laboratorio (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre TEXT
  );

CREATE UNIQUE INDEX laboratorio_ix_1 ON laboratorio (nombre);

CREATE TABLE
  turno (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    usuario_id INTEGER NOT NULL,
    primer_movimiento DATETIME NOT NULL DEFAULT (datetime ('now', 'localtime')),
    monto_caja_inicial INTEGER NOT NULL,
    ultimo_movimiento DATETIME,
    monto_caja_final INTEGER,
    monto_caja_final_real INTEGER,
    comentario TEXT,
    CONSTRAINT usuario_turno FOREIGN KEY (usuario_id) REFERENCES usuario (id)
  );

CREATE TABLE
  movimiento (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    producto_id INTEGER NOT NULL,
    estado_movimiento_id INTEGER NOT NULL,
    tipo_movimiento_id INTEGER NOT NULL,
    documento_id INTEGER NOT NULL,
    turno_id INTEGER NOT NULL,
    momento DATETIME NOT NULL DEFAULT (datetime ('now', 'localtime')),
    producto_nombre TEXT NOT NULL,
    producto_precio INTEGER NOT NULL,
    producto_costo INTEGER NOT NULL,
    precio_cobrado INTEGER NOT NULL,
    multiplicador INTEGER NOT NULL,
    ultimo_precio INTEGER NOT NULL,
    es_salida BOOLEAN NOT NULL,
    CONSTRAINT producto_movimiento FOREIGN KEY (producto_id) REFERENCES producto (id),
    CONSTRAINT estado_movimiento_movimiento FOREIGN KEY (estado_movimiento_id) REFERENCES estado_movimiento (id),
    CONSTRAINT turno_movimiento FOREIGN KEY (turno_id) REFERENCES turno (id),
    CONSTRAINT tipo_movimiento_movimiento FOREIGN KEY (tipo_movimiento_id) REFERENCES tipo_movimiento (id),
    CONSTRAINT documento_movimiento FOREIGN KEY (documento_id) REFERENCES documento (id)
  );

CREATE TABLE
  estado_movimiento (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre TEXT
  );

CREATE TABLE
  principio_activo (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre TEXT NOT NULL
  );

CREATE TABLE
  producto_precio (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    producto_id INTEGER NOT NULL,
    momento DATETIME NOT NULL DEFAULT (datetime ('now', 'localtime')),
    precio_venta_id INTEGER NOT NULL,
    precio_compra INTEGER,
    turno_id INTEGER NOT NULL,
    CONSTRAINT producto_producto_precio FOREIGN KEY (producto_id) REFERENCES producto (id),
    CONSTRAINT turno_producto_precio FOREIGN KEY (turno_id) REFERENCES turno (id)
  );


CREATE TABLE
  categoria_farmacologica (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre TEXT
  );

CREATE UNIQUE INDEX categoria_farmacologica_ix ON categoria_farmacologica (nombre);

CREATE TABLE
  pago (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    tipo_pago_id INTEGER NOT NULL,
    turno_id INTEGER NOT NULL,
    documento_id INTEGER NOT NULL,
    monto INTEGER NOT NULL,
    CONSTRAINT tipo_pago_pago FOREIGN KEY (tipo_pago_id) REFERENCES tipo_pago (id),
    CONSTRAINT documento_documento_id FOREIGN KEY (documento_id) REFERENCES documento (id),
    CONSTRAINT turno_turno_id FOREIGN KEY (turno_id) REFERENCES turno (id)
  );

CREATE TABLE
  tipo_pago (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre TEXT NOT NULL
  );

CREATE TABLE
  tipo_receta (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre TEXT NOT NULL
  );

CREATE TABLE
  tipo_movimiento (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre TEXT
  );

CREATE UNIQUE INDEX estado_movimiento_ix_1 ON tipo_movimiento (nombre);

CREATE TABLE
  cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre TEXT,
    rut TEXT,
    apodo TEXT,
    comentarios TEXT
  );

CREATE TABLE
  detalle_codigo_barras (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    detalle_producto_id INTEGER NOT NULL,
    valor TEXT NOT NULL,
    CONSTRAINT detalle_producto_detalle_codigo_barras FOREIGN KEY (detalle_producto_id) REFERENCES detalle_producto (id)
  );


CREATE TABLE
  detalle_producto (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nombre TEXT NOT NULL
  );