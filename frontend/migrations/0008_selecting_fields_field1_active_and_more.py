# Generated by Django 4.1.7 on 2023-03-21 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0007_selecting_fields_alter_settings_lightnames_field_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='selecting_fields',
            name='field1_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='selecting_fields',
            name='field2_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='selecting_fields',
            name='field3_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='selecting_fields',
            name='field4_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='selecting_fields',
            name='field5_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='selecting_fields',
            name='field6_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='selecting_fields',
            name='field_id',
            field=models.BooleanField(default=False),
        ),
    ]
