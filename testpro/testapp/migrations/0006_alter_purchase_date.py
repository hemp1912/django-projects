# Generated by Django 5.0.3 on 2024-07-13 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_vendor_alter_user_username_purchase_delete_aets_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
