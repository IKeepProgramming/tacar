# Generated by Django 4.1.7 on 2023-04-27 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_veiculo_cliente_id_alter_veiculo_fabricante_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rotativo',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='Total'),
        ),
    ]