# Generated by Django 4.1.7 on 2023-03-23 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0008_selecting_fields_field1_active_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='selecting_fields',
            name='field_id',
        ),
        migrations.AlterField(
            model_name='settings_lightnames',
            name='field_id',
            field=models.CharField(max_length=5),
        ),
    ]