# Generated by Django 4.0.5 on 2022-09-26 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0006_usuario_id_alter_usuario_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='id',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
