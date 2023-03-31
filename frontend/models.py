from django.db import models

class Permissions(models.Model):
    Permission = models.TextField()

    class Meta:
        permissions = (
            ('SystemAdmin', 'SystemAdmin'),
            ('SystemUser', 'SystemUser'),
            ('SystemGuest', 'SystemGuest'),
            ('AddPermissions', 'AddPermissions'),
            ('Database', 'Database'),
        )

    def __str__(self):
        return self.Permission

class Settings_fieldnames(models.Model):
    Veld1 = models.CharField(max_length=10)
    Veld2 = models.CharField(max_length=10)
    Veld3 = models.CharField(max_length=10)
    Veld4 = models.CharField(max_length=10)

    def __str__(self):
        return "Updated_Fieldnames"

    class Meta:
        verbose_name_plural = "Settings Field Names"

class Selecting_fields(models.Model):
    field1_active = models.BooleanField(default = False)
    field2_active = models.BooleanField(default = False)
    field3_active = models.BooleanField(default = False)
    field4_active = models.BooleanField(default = False)
    field5_active = models.BooleanField(default = False)
    field6_active = models.BooleanField(default = False)
    field7_active = models.BooleanField(default = False)
    field8_active = models.BooleanField(default = False)
    field9_active = models.BooleanField(default = False)
    field10_active = models.BooleanField(default = False)
    field11_active = models.BooleanField(default = False)
    field12_active = models.BooleanField(default = False)
    field13_active = models.BooleanField(default = False)
    field14_active = models.BooleanField(default = False)
    field15_active = models.BooleanField(default = False)
    field16_active = models.BooleanField(default = False)
    field17_active = models.BooleanField(default = False)
    field18_active = models.BooleanField(default = False)
    field19_active = models.BooleanField(default = False)
    field20_active = models.BooleanField(default = False)
    field21_active = models.BooleanField(default = False)
    field22_active = models.BooleanField(default = False)
    field23_active = models.BooleanField(default = False)
    field24_active = models.BooleanField(default = False)


class LightButton(models.Model):
    Lamp001_bool = models.BooleanField(default = False)
    Lamp002_bool = models.BooleanField(default = False)
    Lamp003_bool = models.BooleanField(default = False)
    Lamp004_bool = models.BooleanField(default = False)
    Lamp005_bool = models.BooleanField(default = False)
    Lamp006_bool = models.BooleanField(default = False)
    Lamp007_bool = models.BooleanField(default = False)
    Lamp008_bool = models.BooleanField(default = False)
    Lamp009_bool = models.BooleanField(default = False)
    Lamp0010_bool = models.BooleanField(default = False)
    Lamp0011_bool = models.BooleanField(default = False)
    Lamp0012_bool = models.BooleanField(default = False)
    Lamp0013_bool = models.BooleanField(default = False)
    Lamp0014_bool = models.BooleanField(default = False)
    Lamp0015_bool = models.BooleanField(default = False)
    Lamp0016_bool = models.BooleanField(default = False)

    def __str__(self):
        return f'LightButton {self.id}'

class Logo(models.Model):
    logo_image = models.ImageField(null = True, blank = True, upload_to = "IMG/")

    def __str__(self):
        return "Logo"