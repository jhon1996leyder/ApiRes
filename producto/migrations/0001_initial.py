# Generated by Django 4.1.2 on 2022-10-19 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('referencias', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('fechaIngreso', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
