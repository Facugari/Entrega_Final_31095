# Generated by Django 4.0.5 on 2022-09-22 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='contraseña',
            new_name='mensaje',
        ),
    ]
