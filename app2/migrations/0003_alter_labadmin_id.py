# Generated by Django 3.2.4 on 2021-07-07 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_labadmin_lablocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labadmin',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
