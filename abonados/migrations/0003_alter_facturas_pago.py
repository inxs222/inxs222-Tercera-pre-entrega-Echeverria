# Generated by Django 5.0.1 on 2024-02-05 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abonados', '0002_servicios_facturas_pago_alter_facturas_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturas',
            name='pago',
            field=models.BooleanField(),
        ),
    ]