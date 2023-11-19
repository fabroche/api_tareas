# Generated by Django 4.1.7 on 2023-11-19 22:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0013_orden_ordenstatus_ordendetalle_orden_orden_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetodoPago',
            fields=[
                ('id_metodo_pago', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('metodo_pago', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MetodoPagoDetalle',
            fields=[
                ('id_metodo_pago_detalle', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('monto', models.FloatField()),
                ('metodo_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.metodopago')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id_venta', models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('fecha_venta', models.DateTimeField()),
                ('importe_total', models.FloatField()),
                ('salario_del_dia', models.FloatField()),
                ('inversion_total', models.FloatField()),
                ('ganancia_bar', models.FloatField()),
                ('ganancia_alianza', models.FloatField()),
                ('metodo_pago', models.ManyToManyField(to='restaurant.metodopagodetalle')),
                ('orden', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurant.orden')),
            ],
        ),
    ]