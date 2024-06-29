from django.db import models


class lista_con_nombre(models.Model):
  nombre = models.CharField(max_length=64)

  def __str__(self):
    return str(self.nombre)

  class Meta:
    abstract = True
    db_table = ''
    managed = True
    verbose_name = 'lista'
    verbose_name_plural = 'listas'

class principio_activo(lista_con_nombre):
  class Meta:
    verbose_name = 'principio activo'
    verbose_name_plural = 'principios activos'
    

tipo_documento = {
  "FAC":"FACTURA",  
  "BOL":"BOLETA"}
tipo_unidad = (
  "100 G",
  "100 ML",
  "DOSIS",
  "UNIDAD",)

class producto(lista_con_nombre):
  tipo_unidad = models.CharField(max_length=10, choices=tipo_unidad)
  principio_activo = models.ForeignKey(principio_activo, on_delete=models.PROTECT)

  def __str__(self):
    pass

  class Meta:
    db_table = ''
    managed = True
    verbose_name = 'producto'
    verbose_name_plural = 'productos'
