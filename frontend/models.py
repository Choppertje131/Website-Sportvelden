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

class Settings_lightnames(models.Model):
    Lamp1 = models.CharField(max_length=10)
    Lamp2 = models.CharField(max_length=10)
    Lamp3 = models.CharField(max_length=10)
    Lamp4 = models.CharField(max_length=10)
    Lamp5 = models.CharField(max_length=10)
    Lamp6 = models.CharField(max_length=10)
    field_id = models.CharField(max_length=5)

    def __str__(self):
        return self.field_id

    class Meta:
        verbose_name_plural = "Lights fields"

