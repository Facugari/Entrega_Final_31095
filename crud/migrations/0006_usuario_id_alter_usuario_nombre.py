# Generated by Django 4.0.5 on 2022-09-26 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0005_alter_usuario_consulta_alter_usuario_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=20),
        ),
    ]