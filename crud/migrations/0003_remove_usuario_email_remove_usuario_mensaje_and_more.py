# Generated by Django 4.0.5 on 2022-09-22 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_rename_contraseña_usuario_mensaje'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='email',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='mensaje',
        ),
        migrations.AddField(
            model_name='usuario',
            name='consulta',
            field=models.CharField(default=0, max_length=500, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='usuario',
            name='mail',
            field=models.EmailField(default=0, max_length=20),
        ),
    ]
