CREATE EXTENSION IF NOT EXISTS citext;
CREATE EXTENSION IF NOT EXISTS plv8;
CREATE EXTENSION IF NOT EXISTS fuzzystrmatch;

DROP SCHEMA "inventario" CASCADE;
DROP SCHEMA "contabilidad" CASCADE;
DROP SCHEMA "usuarios" CASCADE;
DROP SCHEMA "public" CASCADE;

CREATE SCHEMA IF NOT EXISTS "inventario"
AUTHORIZATION farmacia;    
CREATE SCHEMA IF NOT EXISTS "contabilidad"
AUTHORIZATION farmacia;
CREATE SCHEMA IF NOT EXISTS "usuarios"
AUTHORIZATION farmacia;
CREATE SCHEMA IF NOT EXISTS "public"
AUTHORIZATION farmacia;

CREATE DOMAIN "positivo0" integer
  CONSTRAINT "positivo_cons_1" CHECK(VALUE >= 0);

CREATE DOMAIN "positivo1" integer CONSTRAINT "positivo_cons_1" CHECK(VALUE > 0);

CREATE DOMAIN "email" text
  CONSTRAINT "email_cons_1"
    CHECK ( value ~ '^[a-zA-Z0-9.!#$%&''*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$' );

CREATE DOMAIN "tipo_precio_producto" integer
  CONSTRAINT "tipo_precio_solo_divisible_por_100" CHECK(VALUE % 100 = 0);

CREATE DOMAIN "tipo_monto_retiro" integer
  CONSTRAINT "tipo_precio_solo_divisible_por_10000" CHECK(VALUE % 10000 = 0);


CREATE TYPE "tipo_pago" AS ENUM('EFECTIVO',
'TARJETA',
'TRANSFERENCIA');

CREATE TYPE "unidad_medida" AS ENUM('100 G',
'100 ML',
'DOSIS',
'UNIDAD');

CREATE TYPE "estado_documento" AS ENUM
  ('INVALIDO',
'COTIZANDO',
'PAGANDO',
'FINALIZADO',
'ANULADO');

CREATE TYPE "tipo_documento" AS ENUM
  ('COTIZACION',
'BOLETA',
'FACTURA',
'NOTA CREDITO',
'RETIRO');

CREATE TYPE "tipo_receta" AS ENUM
  ('RMRSCS',
'MRE',
'NP',
'APR',
'WP',
'RMRCCS',
'RCH');

CREATE TYPE "estado_movimiento" AS ENUM
  ('COTIZANDO',
'CORRECTO',
'PENDIENTE',
'ANULADO',
'CANCELADO');

CREATE TYPE "tipo_movimiento" AS ENUM('VENTA',
'COMPRA');

CREATE TYPE "tipo_persona" AS ENUM('INTERNO',
'CLIENTE',
'TRANSFERENCIA');

CREATE TYPE "tipo_usuario" AS ENUM('VENDEDORES',
'JEFES',
'ACCESO_TOTAL');

CREATE TABLE IF NOT EXISTS "inventario"."categoria_farmacologica"(
  "categoria_farmacologica_id" serial NOT NULL,
  "nombre" text NOT NULL,
  CONSTRAINT "pk_1482" PRIMARY KEY("categoria_farmacologica_id")
);

CREATE TABLE IF NOT EXISTS "usuarios"."cliente"(
  "cliente_id" integer NOT NULL,
  "apodo" text,
  "comentarios" text,
  CONSTRAINT "pk_1198" PRIMARY KEY("cliente_id")
);

CREATE TABLE IF NOT EXISTS "inventario"."codigo_de_barras"(
  "codigo_de_barras_id" character varying(24) NOT NULL,
  "producto_id" integer NOT NULL,
  "laboratorio_id" integer NOT NULL,
  "ultimo_movimiento_salida_id" integer NOT NULL,
  "ultimo_movimiento_entrada_id" integer NOT NULL,
  "reg_isp" character varying(10),
  "es_generico" boolean,
  "es_cenabast" boolean,
  "es_bioequivalente" boolean,
  "miligramos_peso" "positivo1",
  "precio" "tipo_precio_producto",
  CONSTRAINT "pk_1353" PRIMARY KEY("codigo_de_barras_id")
);

  CREATE INDEX IF NOT EXISTS "codigo_de_barras_ix_1" ON "inventario"."codigo_de_barras"
    ("producto_id");
  
CREATE TABLE IF NOT EXISTS "comentario"(
  "tabla" name NOT NULL,
  "objeto_id" integer NOT NULL,
  "momento" timestamp NOT NULL DEFAULT now(),
  "comentario" text NOT NULL,
  CONSTRAINT "comentarios1_pkey" PRIMARY KEY(
    "tabla",
    "objeto_id"
  )
);

  CREATE INDEX IF NOT EXISTS "comentario_momento_idx" ON "comentario"("momento" DESC);
  
CREATE TABLE IF NOT EXISTS "contabilidad"."detalle_factura_recepcion"(
  "detalle_factura_recepcion_id" serial NOT NULL,
  "factura_recepcion_id" integer NOT NULL,
  "producto_id" integer NOT NULL,
  "movimiento_id" integer,
  "nombre" character varying(64) NOT NULL,
  "monto_total" "positivo1" NOT NULL,
  "cantidad_teorico" "positivo1" NOT NULL DEFAULT 1,
  "cantidad_fisico" "positivo0" NOT NULL,
  "codigo_del_proveedor" character varying(64),
  CONSTRAINT "pk_1982" PRIMARY KEY("detalle_factura_recepcion_id")
);

CREATE TABLE IF NOT EXISTS "contabilidad"."documento"(
  "documento_id" serial NOT NULL,
  "turno_id" integer NOT NULL,
  "cliente_id" integer NOT NULL,
  "momento" timestamp NOT NULL DEFAULT NOW(),
  "total_documento" "positivo1" NOT NULL,
  "comentario" text,
  "tipo_documento" "tipo_documento" NOT NULL,
  "estado_documento" "estado_documento" NOT NULL,
  CONSTRAINT "pk_1099" PRIMARY KEY("documento_id")
);

  CREATE INDEX IF NOT EXISTS "documento_momento_idx" ON "contabilidad"."documento"
    ("momento" DESC);
  
  CREATE INDEX IF NOT EXISTS "documento_turno_idx" ON "contabilidad"."documento"("turno_id");
  
CREATE TABLE IF NOT EXISTS "contabilidad"."factura_recepcion"(
  "factura_recepcion_id" serial NOT NULL,
  "proveedor_id" integer NOT NULL,
  "usuario_id" integer NOT NULL,
  "folio" "positivo1",
  "fecha" date NOT NULL,
  "monto_total" integer,
  "raw_xml" xml,
  "momento" timestamp DEFAULT NOW(),
  CONSTRAINT "pk_1403" PRIMARY KEY("factura_recepcion_id")
);

CREATE TABLE IF NOT EXISTS "inventario"."forma_farmaceutica"(
  "forma_farmaceutica_id" serial NOT NULL,
  "nombre" text NOT NULL,
  "unidad_medida" "unidad_medida" NOT NULL,
  CONSTRAINT "pk_1391" PRIMARY KEY("forma_farmaceutica_id")
);

CREATE TABLE IF NOT EXISTS "usuarios"."laboratorio"(
  "laboratorio_id" serial NOT NULL,
  "nombre" character varying(20) NOT NULL,
  CONSTRAINT "pk_1377" PRIMARY KEY("laboratorio_id")
);

CREATE TABLE IF NOT EXISTS "momento"(
  "tabla" name NOT NULL,
  "objeto_id" integer NOT NULL,
  "momento" timestamp NOT NULL DEFAULT NOW(),
  CONSTRAINT "comentarios1_pkey" PRIMARY KEY(
    "tabla",
    "objeto_id"
  )
);

  CREATE INDEX IF NOT EXISTS "comentario_momento_idx" ON "momento"("momento" DESC);
  
CREATE TABLE IF NOT EXISTS "inventario"."movimiento"(
  "movimiento_id" serial NOT NULL,
  "producto_id" integer NOT NULL,
  "usuario_id" integer NOT NULL,
  "documento_id" integer NOT NULL,
  "turno_id" integer NOT NULL,
  "momento" timestamp NOT NULL DEFAULT NOW(),
  "producto_precio" "positivo1" NOT NULL,
  "producto_costo" "positivo1" NOT NULL,
  "precio_efectivo" "tipo_precio_producto" NOT NULL,
  "cantidad" "positivo1" NOT NULL CHECK ( cantidad > 0),
  "ultimo_precio" "positivo1" NOT NULL,
  "es_salida" boolean NOT NULL,
  "estado_movimiento" "estado_movimiento" NOT NULL,
  "tipo_movimiento" "tipo_movimiento" NOT NULL,
  CONSTRAINT "pk_1893" PRIMARY KEY("movimiento_id")
);

CREATE TABLE IF NOT EXISTS "contabilidad"."pago"(
  "pago_id" serial NOT NULL,
  "turno_id" integer NOT NULL,
  "documento_id" integer NOT NULL,
  "monto" "positivo1" NOT NULL,
  "tipo_pago" "tipo_pago" NOT NULL,
  CONSTRAINT "pk_1319" PRIMARY KEY("pago_id")
);

CREATE TABLE IF NOT EXISTS "contabilidad"."pedido"(
  "pedido_id" serial NOT NULL,
  "turno_id" integer NOT NULL,
  "usuario_id" integer NOT NULL,
  "producto_id" integer NOT NULL,
  "producto_nombre" character varying(64) NOT NULL,
  "listo" boolean NOT NULL,
  "momento" timestamp NOT NULL DEFAULT NOW(),
  "cantidad" "positivo1",
  CONSTRAINT "pk_1522" PRIMARY KEY("pedido_id")
);

CREATE TABLE IF NOT EXISTS "usuarios"."persona"(
  "persona_id" serial NOT NULL,
  "responsable" integer NOT NULL,
  "nombre_apellido" character varying(64),
  "email" "email",
  "apodo" character varying(16) NOT NULL,
  "direccion" character varying(80),
  "momento" timestamp DEFAULT NOW(),
  "telefonos" character varying(18)[],
  CONSTRAINT "pk_1573" PRIMARY KEY("persona_id")
);

CREATE TABLE IF NOT EXISTS "inventario"."principio_activo"(
  "principio_activo_id" serial NOT NULL,
  "nombre" text NOT NULL,
  CONSTRAINT "pk_1921" PRIMARY KEY("principio_activo_id")
);

CREATE TABLE IF NOT EXISTS "contabilidad"."producto"(
  "producto_id" serial NOT NULL,
  "nombre" character varying(64) NOT NULL,
  "categoria_farmacologica_id" integer,
  "forma_farmaceutica_id" integer,
  "principio_activo_id" integer,
  "es_controlado" boolean,
  "es_refrigerado" boolean,
  "es_generico" boolean,
  "cantidad_por_envase" "positivo1",
  "tipo_receta" "tipo_receta",
  "precio_defecto" "tipo_precio_producto",
  CONSTRAINT "pk_1154" PRIMARY KEY("producto_id")
);

CREATE TABLE IF NOT EXISTS "contabilidad"."producto_precio"(
  "producto_precio_id" serial NOT NULL,
  "turno_id" integer NOT NULL,
  "usuario_id" integer NOT NULL,
  "codigo_de_barras_id" character varying(24) NOT NULL,
  "movimiento_movimiento_id" integer,
  "momento" timestamp NOT NULL DEFAULT NOW(),
  "precio" "tipo_precio_producto" NOT NULL,
  "es_automatico" bool NOT NULL DEFAULT TRUE,
  "es_precio_compra" bool NOT NULL,
  CONSTRAINT "pk_1404" PRIMARY KEY("producto_precio_id")
);

  CREATE UNIQUE INDEX IF NOT EXISTS "timestamp_y_producto" ON "contabilidad"."producto_precio"(
    "momento" DESC,
    "codigo_de_barras_id",
    "es_precio_compra"
  );
  
CREATE TABLE IF NOT EXISTS "usuarios"."proveedores"(
  "proveedor_id" serial NOT NULL,
  "cuenta_pagos" text,
  CONSTRAINT "pk_1239" PRIMARY KEY("proveedor_id")
);

CREATE TABLE IF NOT EXISTS "contabilidad"."retiro"(
  "id" serial NOT NULL,
  "usuario_id" integer NOT NULL,
  "documento_id" integer NOT NULL,
  "turno_id" integer NOT NULL,
  "monto" "tipo_monto_retiro" NOT NULL,
  "momento" timestamp NOT NULL DEFAULT NOW(),
  CONSTRAINT "retiro_pk" PRIMARY KEY("id")
);

  CREATE UNIQUE INDEX IF NOT EXISTS "retiro_ix_1" ON "contabilidad"."retiro"("momento" DESC);
  
CREATE TABLE IF NOT EXISTS "contabilidad"."turno"(
  "turno_id" serial NOT NULL,
  "usuario_id" integer NOT NULL,
  "momento" timestamp NOT NULL DEFAULT NOW(),
  "monto_caja_inicial" integer NOT NULL,
  "ultimo_movimiento" timestamp,
  "monto_caja_final" integer,
  "monto_caja_final_real" integer,
  CONSTRAINT "pk_1904" PRIMARY KEY("turno_id")
);

  CREATE UNIQUE INDEX IF NOT EXISTS "momento_turno_idx" ON "contabilidad"."turno"("momento");
  
CREATE TABLE IF NOT EXISTS "usuarios"."usuario"(
  "usuario_id" integer NOT NULL,
  "tipo_usuario" "tipo_usuario",
  CONSTRAINT "pk_1612" PRIMARY KEY("usuario_id")
);

  CREATE UNIQUE INDEX IF NOT EXISTS "usuario_ix_1" ON "usuarios"."usuario";
  
ALTER TABLE "contabilidad"."documento"
  ADD CONSTRAINT IF NOTE EXISTS "cliente_documento"
    FOREIGN KEY ("cliente_id") REFERENCES "usuarios"."cliente" ("cliente_id");

ALTER TABLE "contabilidad"."pago"
  ADD CONSTRAINT "documento_documento_id"
    FOREIGN KEY ("documento_id")
      REFERENCES "contabilidad"."documento" ("documento_id");

ALTER TABLE "inventario"."movimiento"
  ADD CONSTRAINT "documento_movimiento"
    FOREIGN KEY ("documento_id")
      REFERENCES "contabilidad"."documento" ("documento_id");

ALTER TABLE "contabilidad"."detalle_factura_recepcion"
  ADD CONSTRAINT "factura_compra_detalle_factura_compra"
    FOREIGN KEY ("factura_recepcion_id")
      REFERENCES "contabilidad"."factura_recepcion" ("factura_recepcion_id");

ALTER TABLE "contabilidad"."producto"
  ADD CONSTRAINT "forma_farmaceutica_producto"
    FOREIGN KEY ("forma_farmaceutica_id")
      REFERENCES "inventario"."forma_farmaceutica" ("forma_farmaceutica_id");

ALTER TABLE "contabilidad"."producto"
  ADD CONSTRAINT "id_producto"
    FOREIGN KEY ("categoria_farmacologica_id")
      REFERENCES "inventario"."categoria_farmacologica" ("categoria_farmacologica_id")
  ;

ALTER TABLE "contabilidad"."detalle_factura_recepcion"
  ADD CONSTRAINT "movimiento_detalle_factura_compra"
    FOREIGN KEY ("movimiento_id")
      REFERENCES "inventario"."movimiento" ("movimiento_id");

ALTER TABLE "contabilidad"."producto"
  ADD CONSTRAINT "principio_activo_producto"
    FOREIGN KEY ("principio_activo_id")
      REFERENCES "inventario"."principio_activo" ("principio_activo_id");

ALTER TABLE "contabilidad"."detalle_factura_recepcion"
  ADD CONSTRAINT "producto_detalle_factura_compra"
    FOREIGN KEY ("producto_id") REFERENCES "contabilidad"."producto" ("producto_id")
  ;

ALTER TABLE "inventario"."movimiento"
  ADD CONSTRAINT "producto_movimiento"
    FOREIGN KEY ("producto_id") REFERENCES "contabilidad"."producto" ("producto_id")
  ;

ALTER TABLE "contabilidad"."pedido"
  ADD CONSTRAINT "producto_producto_id"
    FOREIGN KEY ("producto_id") REFERENCES "contabilidad"."producto" ("producto_id")
  ;

ALTER TABLE "inventario"."codigo_de_barras"
  ADD CONSTRAINT "productos_codigos_de_barra"
    FOREIGN KEY ("producto_id") REFERENCES "contabilidad"."producto" ("producto_id")
  ;

ALTER TABLE "contabilidad"."factura_recepcion"
  ADD CONSTRAINT "proveedores_facturas_compra"
    FOREIGN KEY ("proveedor_id")
      REFERENCES "usuarios"."proveedores" ("proveedor_id");

ALTER TABLE "contabilidad"."documento"
  ADD CONSTRAINT "turno_documento"
    FOREIGN KEY ("turno_id") REFERENCES "contabilidad"."turno" ("turno_id");

ALTER TABLE "inventario"."movimiento"
  ADD CONSTRAINT "turno_movimiento"
    FOREIGN KEY ("turno_id") REFERENCES "contabilidad"."turno" ("turno_id");

ALTER TABLE "contabilidad"."producto_precio"
  ADD CONSTRAINT "turno_producto_precio"
    FOREIGN KEY ("turno_id") REFERENCES "contabilidad"."turno" ("turno_id");

ALTER TABLE "contabilidad"."pago"
  ADD CONSTRAINT "turno_turno_id"
    FOREIGN KEY ("turno_id") REFERENCES "contabilidad"."turno" ("turno_id");

ALTER TABLE "contabilidad"."pedido"
  ADD CONSTRAINT "turno_turno_id"
    FOREIGN KEY ("turno_id") REFERENCES "contabilidad"."turno" ("turno_id");

ALTER TABLE "contabilidad"."factura_recepcion"
  ADD CONSTRAINT "usuario_factura_recepcion"
    FOREIGN KEY ("usuario_id") REFERENCES "usuarios"."usuario" ("usuario_id");

ALTER TABLE "contabilidad"."turno"
  ADD CONSTRAINT "usuario_turno"
    FOREIGN KEY ("usuario_id") REFERENCES "usuarios"."usuario" ("usuario_id");

ALTER TABLE "inventario"."codigo_de_barras"
  ADD CONSTRAINT "laboratorio_codigo_de_barras"
    FOREIGN KEY ("laboratorio_id")
      REFERENCES "usuarios"."laboratorio" ("laboratorio_id");

ALTER TABLE "inventario"."movimiento"
  ADD CONSTRAINT "usuario_movimiento"
    FOREIGN KEY ("usuario_id") REFERENCES "usuarios"."usuario" ("usuario_id");

ALTER TABLE "inventario"."codigo_de_barras"
  ADD CONSTRAINT "movimiento_codigo_de_barras"
    FOREIGN KEY ("ultimo_movimiento_salida_id")
      REFERENCES "inventario"."movimiento" ("movimiento_id");

ALTER TABLE "inventario"."codigo_de_barras"
  ADD CONSTRAINT "movimiento_codigo_de_barras"
    FOREIGN KEY ("ultimo_movimiento_entrada_id")
      REFERENCES "inventario"."movimiento" ("movimiento_id");

ALTER TABLE "contabilidad"."producto_precio"
  ADD CONSTRAINT "codigo_de_barras_producto_precio"
    FOREIGN KEY ("codigo_de_barras_id")
      REFERENCES "inventario"."codigo_de_barras" ("codigo_de_barras_id");

ALTER TABLE "contabilidad"."producto_precio"
  ADD CONSTRAINT "usuario_producto_precio"
    FOREIGN KEY ("usuario_id") REFERENCES "usuarios"."usuario" ("usuario_id");

ALTER TABLE "contabilidad"."producto_precio"
  ADD CONSTRAINT "movimiento_producto_precio"
    FOREIGN KEY ("movimiento_movimiento_id")
      REFERENCES "inventario"."movimiento" ("movimiento_id");

ALTER TABLE "usuarios"."usuario"
  ADD CONSTRAINT "persona_usuario"
    FOREIGN KEY ("usuario_id") REFERENCES "usuarios"."persona" ("persona_id");

ALTER TABLE "usuarios"."cliente"
  ADD CONSTRAINT "persona_cliente"
    FOREIGN KEY ("cliente_id") REFERENCES "usuarios"."persona" ("persona_id");

ALTER TABLE "usuarios"."proveedores"
  ADD CONSTRAINT "persona_proveedores"
    FOREIGN KEY ("proveedor_id") REFERENCES "usuarios"."persona" ("persona_id");

ALTER TABLE "contabilidad"."retiro"
  ADD CONSTRAINT "usuario_retiro"
    FOREIGN KEY ("usuario_id") REFERENCES "usuarios"."usuario" ("usuario_id");

ALTER TABLE "contabilidad"."retiro"
  ADD CONSTRAINT "documento_retiro"
    FOREIGN KEY ("documento_id")
      REFERENCES "contabilidad"."documento" ("documento_id");

ALTER TABLE "contabilidad"."retiro"
  ADD CONSTRAINT "turno_retiro"
    FOREIGN KEY ("turno_id") REFERENCES "contabilidad"."turno" ("turno_id");

ALTER TABLE "usuarios"."persona"
  ADD CONSTRAINT "usuario_persona"
    FOREIGN KEY ("responsable") REFERENCES "usuarios"."usuario" ("usuario_id");

ALTER TABLE "contabilidad"."pedido"
  ADD CONSTRAINT "usuario_pedido"
    FOREIGN KEY ("usuario_id") REFERENCES "usuarios"."usuario" ("usuario_id");
