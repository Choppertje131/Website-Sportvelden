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

    def _str_(self):
        return self.Settings_fieldnames

    class Meta:
        verbose_name_plural = "Settings Field Names"

class Settings_lightnames(models.Model):
    Lamp1 = models.CharField(max_length=10)
    Lamp2 = models.CharField(max_length=10)
    Lamp3 = models.CharField(max_length=10)
    Lamp4 = models.CharField(max_length=10)
    Lamp5 = models.CharField(max_length=10)
    Lamp6 = models.CharField(max_length=10)
    Lamp7 = models.CharField(max_length=10)
    Lamp8 = models.CharField(max_length=10)
    Lamp9 = models.CharField(max_length=10)
    Lamp10 = models.CharField(max_length=10)
    Lamp11 = models.CharField(max_length=10)
    Lamp12 = models.CharField(max_length=10)
    Lamp13 = models.CharField(max_length=10)
    Lamp14 = models.CharField(max_length=10)
    Lamp15 = models.CharField(max_length=10)
    Lamp16 = models.CharField(max_length=10)
    Lamp17 = models.CharField(max_length=10)
    Lamp18 = models.CharField(max_length=10)
    Lamp19 = models.CharField(max_length=10)
    Lamp20 = models.CharField(max_length=10)

    def _str_(self):
        return self.lights_fields

    class Meta:
        verbose_name_plural = "Lights fields"

