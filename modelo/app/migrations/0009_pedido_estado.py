# Generated by Django 4.0.4 on 2022-06-16 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_carrito_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='estado',
            field=models.IntegerField(choices=[(1, 'Preparacion'), (2, 'En reparto'), (3, 'Entregado')], default=0),
        ),
    ]
