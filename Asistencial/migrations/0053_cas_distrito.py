# Generated by Django 3.1.1 on 2023-03-16 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asistencial', '0052_auto_20230313_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='cas',
            name='distrito',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
