# Generated by Django 5.0.6 on 2024-07-01 17:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaFarmacologica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'categoria_farmacologica',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(unique=True)),
                ('rut', models.TextField(blank=True, null=True)),
                ('apodo', models.TextField(blank=True, null=True)),
                ('comentarios', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cliente',
            },
        ),
        migrations.CreateModel(
            name='DetalleProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'detalle_producto',
            },
        ),
        migrations.CreateModel(
            name='EstadoDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'estado_documento',
            },
        ),
        migrations.CreateModel(
            name='EstadoMovimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'estado_movimiento',
            },
        ),
        migrations.CreateModel(
            name='FormaFarmaceutica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'forma_farmaceutica',
            },
        ),
        migrations.CreateModel(
            name='Laboratorio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'laboratorio',
            },
        ),
        migrations.CreateModel(
            name='PrincipioActivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'principio_activo',
            },
        ),
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'tipo_documento',
            },
        ),
        migrations.CreateModel(
            name='TipoMovimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'tipo_movimiento',
            },
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'tipo_pago',
            },
        ),
        migrations.CreateModel(
            name='TipoReceta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'tipo_receta',
            },
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primer_movimiento', models.DateTimeField()),
                ('monto_caja_inicial', models.IntegerField()),
                ('ultimo_movimiento', models.DateTimeField(blank=True, null=True)),
                ('monto_caja_final', models.IntegerField(blank=True, null=True)),
                ('monto_caja_final_real', models.IntegerField(blank=True, null=True)),
                ('comentario', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'turno',
            },
        ),
        migrations.CreateModel(
            name='UnidadMedida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'unidad_medida',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(unique=True)),
                ('rut', models.TextField()),
                ('apodo', models.TextField()),
            ],
            options={
                'db_table': 'usuario',
            },
        ),
        migrations.CreateModel(
            name='DetalleCodigoBarras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.TextField()),
                ('detalle_producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.detalleproducto')),
            ],
            options={
                'db_table': 'detalle_codigo_barras',
            },
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('momento', models.DateTimeField()),
                ('total_documento', models.IntegerField()),
                ('comentario', models.TextField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.cliente')),
                ('estado_documento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.estadodocumento')),
                ('tipo_documento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.tipodocumento')),
                ('turno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.turno')),
            ],
            options={
                'db_table': 'documento',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(unique=True)),
                ('pharmid', models.TextField(blank=True, null=True)),
                ('registro_isp', models.TextField(blank=True, null=True)),
                ('es_cenabast', models.BooleanField(blank=True, null=True)),
                ('es_controlado', models.BooleanField(blank=True, null=True)),
                ('es_refrigerado', models.BooleanField(blank=True, null=True)),
                ('es_bioequivalente', models.BooleanField(blank=True, null=True)),
                ('es_generico', models.BooleanField(blank=True, null=True)),
                ('cantidad_por_envase', models.IntegerField(blank=True, null=True)),
                ('categoria_farmacologica', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.categoriafarmacologica')),
                ('forma_farmaceutica', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.formafarmaceutica')),
                ('laboratorio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.laboratorio')),
                ('principio_activo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.principioactivo')),
                ('tipo_receta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.tiporeceta')),
            ],
            options={
                'db_table': 'producto',
            },
        ),
        migrations.CreateModel(
            name='CodigoDeBarras',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('detalle_codigo_barras', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.detallecodigobarras')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.producto')),
            ],
            options={
                'db_table': 'codigo_de_barras',
            },
        ),
        migrations.CreateModel(
            name='ProductoPrecio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('momento', models.DateTimeField()),
                ('precio_venta', models.IntegerField()),
                ('precio_compra', models.IntegerField(blank=True, null=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.producto')),
                ('turno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.turno')),
            ],
            options={
                'db_table': 'producto_precio',
            },
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.IntegerField()),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.documento')),
                ('tipo_pago', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.tipopago')),
                ('turno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.turno')),
            ],
            options={
                'db_table': 'pago',
            },
        ),
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('momento', models.DateTimeField()),
                ('producto_nombre', models.TextField()),
                ('producto_precio', models.IntegerField()),
                ('producto_costo', models.IntegerField()),
                ('precio_cobrado', models.IntegerField()),
                ('multiplicador', models.IntegerField()),
                ('ultimo_precio', models.IntegerField()),
                ('es_salida', models.BooleanField()),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.documento')),
                ('estado_movimiento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.estadomovimiento')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.producto')),
                ('tipo_movimiento', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.tipomovimiento')),
                ('turno', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.turno')),
            ],
            options={
                'db_table': 'movimiento',
            },
        ),
        migrations.AddField(
            model_name='formafarmaceutica',
            name='unidad_de_medida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.unidadmedida'),
        ),
        migrations.AddField(
            model_name='turno',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='inventario.usuario'),
        ),
    ]
