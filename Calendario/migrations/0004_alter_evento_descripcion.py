# Generated by Django 5.1.1 on 2024-11-25 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calendario', '0003_alter_evento_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='descripcion',
            field=models.CharField(max_length=50),
        ),
    ]
