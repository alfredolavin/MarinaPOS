# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class lista_nombres(models.Model):
  nombre = models.TextField(unique=True, blank=False, null=False)

  def __str__(self):
    return self.nombre

  class Meta:
    abstract=True

class CategoriaFarmacologica(lista_nombres):

  class Meta:
    db_table = 'categoria_farmacologica'


class CodigoDeBarras(models.Model):
  id = models.TextField(primary_key=True)
  producto = models.ForeignKey('Producto', models.PROTECT)

  class Meta:
    db_table = 'codigo_de_barras'


class Documento(models.Model):
  turno = models.ForeignKey('Turno', models.PROTECT)
  tipo_documento = models.ForeignKey('TipoDocumento', models.PROTECT)
  estado_documento = models.ForeignKey('EstadoDocumento', models.PROTECT)
  momento = models.DateTimeField(auto_now=True)
  total_documento = models.PositiveIntegerField()
  comentario = models.TextField(blank=True, null=True)

  class Meta:
    db_table = 'documento'


class EstadoDocumento(lista_nombres):

  class Meta:
    db_table = 'estado_documento'


class EstadoMovimiento(lista_nombres):

  class Meta:
    db_table = 'estado_movimiento'


class FormaFarmaceutica(lista_nombres):
  unidad_de_medida = models.ForeignKey('UnidadMedida', models.PROTECT)

  class Meta:
    db_table = 'forma_farmaceutica'


class Laboratorio(lista_nombres):
  
  class Meta:
    db_table = 'laboratorio'


class Movimiento(models.Model):
  producto = models.ForeignKey('Producto', models.PROTECT)
  turno = models.ForeignKey('Turno', models.PROTECT)
  documento = models.ForeignKey(Documento, models.PROTECT)
  estado_movimiento = models.ForeignKey(EstadoMovimiento, models.PROTECT)
  producto_nombre = models.TextField()
  producto_precio = models.PositiveIntegerField()
  producto_costo = models.PositiveIntegerField()
  precio_cobrado = models.PositiveIntegerField()
  multiplicador = models.PositiveIntegerField()

  class Meta:
    db_table = 'movimiento'


class Pago(models.Model):
  monto = models.PositiveIntegerField(blank=True, null=True)
  documento = models.ForeignKey(Documento, models.PROTECT)
  tipo_pago = models.ForeignKey('TipoPago', models.PROTECT)
  turno = models.ForeignKey('Turno', models.PROTECT)

  class Meta:
    db_table = 'pago'


class PrincipioActivo(lista_nombres):

  class Meta:
    db_table = 'principio_activo'


class Producto(models.Model):
  pharmid = models.TextField(blank=True, default="")
  nombre = models.TextField(blank=False)
  laboratorio = models.ForeignKey(Laboratorio, models.PROTECT)
  categoria_farmacologica = models.ForeignKey(CategoriaFarmacologica, models.PROTECT)
  forma_farmaceutica = models.ForeignKey(FormaFarmaceutica, models.PROTECT)
  principio_activo = models.ForeignKey(PrincipioActivo, models.PROTECT)
  tipo_receta = models.ForeignKey('TipoReceta', models.PROTECT)
  registro_isp = models.TextField(blank=True, null=True)
  es_cenabast = models.BooleanField(blank=True, null=True)
  es_controlado = models.BooleanField(blank=True, null=True)
  es_refrigerado = models.BooleanField(blank=True, null=True)
  es_bioequivalente = models.BooleanField(blank=True, null=True)
  es_generico = models.BooleanField(blank=True, null=True)
  cantidad_por_envase = models.PositiveIntegerField(blank=True, null=True)

  class Meta:
    db_table = 'producto'


class ProductoPrecio(models.Model):
  producto = models.ForeignKey(Producto, models.PROTECT)
  momento = models.DateTimeField(auto_now=True)
  precio_venta = models.PositiveIntegerField()
  precio_compra = models.PositiveIntegerField(blank=True, null=True)
  turno = models.ForeignKey('Turno', models.PROTECT)

  class Meta:
    db_table = 'producto_precio'


class TipoDocumento(lista_nombres):

  class Meta:
    db_table = 'tipo_documento'


class TipoPago(lista_nombres):

  class Meta:
    db_table = 'tipo_pago'


class TipoReceta(lista_nombres):

  class Meta:
    db_table = 'tipo_receta'


class Turno(models.Model):
  usuario = models.ForeignKey('Usuario', models.PROTECT)
  primer_movimiento = models.DateTimeField(auto_now=True)
  monto_caja_inicial = models.PositiveIntegerField()
  ultimo_movimiento = models.DateTimeField(blank=True, null=True)
  monto_caja_final = models.PositiveIntegerField(blank=True, null=True)
  monto_caja_final_real = models.PositiveIntegerField(blank=True, null=True)
  comentario = models.TextField(blank=True, null=True)

  class Meta:
    db_table = 'turno'


class UnidadMedida(lista_nombres):

  class Meta:
    db_table = 'unidad_medida'


class Usuario(models.Model):
  nombre = models.TextField()
  rut = models.TextField()
  apodo = models.TextField()

  class Meta:
    db_table = 'usuario'
