# Generated by Django 5.0.3 on 2024-07-14 05:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0007_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='vendor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='testapp.vendor'),
        ),
    ]
