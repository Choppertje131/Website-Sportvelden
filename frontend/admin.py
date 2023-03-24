from django.contrib import admin
from .models import Permissions
from .models import Settings_fieldnames
from .models import Settings_lightnames
from .models import Selecting_fields
from .models import LightButton

# Register your models here.
admin.site.register(Permissions)
admin.site.register(Settings_fieldnames)
admin.site.register(Settings_lightnames)
admin.site.register(Selecting_fields)
admin.site.register(LightButton)