from django.contrib import admin
from .models import Permissions
from .models import Settings_fieldnames
from .models import Settings_lightnames

# Register your models here.
admin.site.register(Permissions)
admin.site.register(Settings_fieldnames)
admin.site.register(Settings_lightnames)
