# Generated by Django 4.1.6 on 2023-02-09 20:21

from django.db import migrations
import psqlextra.manager.manager


class Migration(migrations.Migration):

    dependencies = [
        ('gestionUsuarios', '0002_alter_usuarios_edad'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='usuarios',
            managers=[
                ('beer', psqlextra.manager.manager.PostgresManager()),
            ],
        ),
    ]