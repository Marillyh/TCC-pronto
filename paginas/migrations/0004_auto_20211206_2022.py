# Generated by Django 2.2.24 on 2021-12-06 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0003_auto_20211202_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=models.FileField(upload_to='media'),
        ),
    ]
