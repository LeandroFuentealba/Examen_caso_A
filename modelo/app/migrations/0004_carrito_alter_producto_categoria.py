# Generated by Django 4.0.4 on 2022-06-12 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_producto_categoria_alter_cliente_nombreusuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('idusuario', models.CharField(max_length=50)),
                ('idprod', models.CharField(max_length=50)),
                ('candtidad', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.categoria'),
        ),
    ]