# Generated by Django 3.1.1 on 2022-12-30 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencial', '0041_auto_20221220_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutricion',
            name='obsNutricion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
