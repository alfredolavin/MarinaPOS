CREATE TABLE producto(
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  nombre TEXT,
  precio INTEGER,
  costo INTEGER,
  stock INTEGER,
  registro_isp TEXT
);

  CREATE INDEX productos_ix_1 ON producto(nombre);
  
CREATE TABLE codigos_de_barra(
  id TEXT NOT NULL,
  producto_id INTEGER NOT NULL,
  multiplicador INTEGER NOT NULL DEFAULT 1,
  CONSTRAINT productos_codigos_de_barra
    FOREIGN KEY (producto_id) REFERENCES producto (id)
);

CREATE TABLE documento(
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  momento TEXT DEFAULT CURRENT_TIMESTAMP,
  usuario_id INTEGER NOT NULL,
  nombre_usuario INTEGER,
  tipo_de_pago_id INTEGER NOT NULL,
  total_documento INTEGER,
  costo_total INTEGER,
  tipo_documento_id INTEGER NOT NULL,
  estado_documento_id INTEGER NOT NULL,
  CONSTRAINT usuarios_ventas FOREIGN KEY (usuario_id) REFERENCES usuario (id),
  CONSTRAINT tipos_de_pago_ventas
    FOREIGN KEY (tipo_de_pago_id) REFERENCES tipo_de_pago (id),
  CONSTRAINT tipo_documento_documento
    FOREIGN KEY (tipo_documento_id) REFERENCES tipo_documento (id),
  CONSTRAINT estado_documento_documento
    FOREIGN KEY (estado_documento_id) REFERENCES estado_documento (id)
);

  CREATE INDEX documentos_ix_1 ON documento(momento);
  
  CREATE INDEX documentos_ix_2 ON documento(usuario_id);
  
CREATE TABLE detalle_documento(
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  ventas_id INTEGER NOT NULL,
  producto_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  nombre_producto TEXT,
  cantidad INTEGER NOT NULL DEFAULT 1,
  precio_base INTEGER,
  precio INTEGER NOT NULL,
  costo INTEGER NOT NULL,
  momento TEXT DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT ventas_detalle_venta
    FOREIGN KEY (ventas_id) REFERENCES documento (id),
  CONSTRAINT productos_detalle_venta
    FOREIGN KEY (producto_id) REFERENCES producto (id)
);

  CREATE INDEX detalle_venta_ix_1 ON detalle_documento(ventas_id);
  
CREATE TABLE usuario(
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  nombre TEXT NOT NULL,
  momento_creacion TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  rut TEXT NOT NULL,
  apodo TEXT NOT NULL
);

CREATE TABLE tipo_de_pago
  (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nombre TEXT NOT NULL);

CREATE TABLE principio_activo_vs_producto(
  producto_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  principio_activo_id INTEGER NOT NULL,
  CONSTRAINT productos_principio_activo_vs_producto
    FOREIGN KEY (producto_id) REFERENCES producto (id),
  CONSTRAINT principio_activo_principio_activo_vs_producto
    FOREIGN KEY (principio_activo_id) REFERENCES principio_activo (id)
);

CREATE TABLE principio_activo
  (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nombre TEXT NOT NULL);

  CREATE INDEX principio_activo_ix_1 ON principio_activo(nombre);
  
CREATE TABLE familia_producto(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nombre INTEGER NOT NULL,
  "codigo_ATC" INTEGER
);

CREATE TABLE tipo_documento
  (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nombre INTEGER);

CREATE TABLE familia_producto_vs_producto(
  producto_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  familia_producto_id INTEGER NOT NULL,
  CONSTRAINT producto_familia_producto_vs_producto
    FOREIGN KEY (producto_id) REFERENCES producto (id),
  CONSTRAINT familia_producto_familia_producto_vs_producto
    FOREIGN KEY (familia_producto_id) REFERENCES familia_producto (id)
);

CREATE TABLE estado_documento
  (id INTEGER NOT NULL, nombre INTEGER, PRIMARY KEY(id));
