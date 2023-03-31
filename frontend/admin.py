from django.contrib import admin
from .models import Permissions
from .models import Settings_fieldnames
from .models import Selecting_fields
from .models import LightButton
from .models import Logo
from django.conf import settings
from django.contrib.admin.options import ModelAdmin
from django.utils.html import format_html

# Register your models here.
admin.site.register(Permissions)
admin.site.register(Settings_fieldnames)
admin.site.register(Selecting_fields)
admin.site.register(LightButton)
admin.site.register(Logo)

class MyModelAdmin(ModelAdmin):
    class Media:
        js = [
            'https://code.jquery.com/jquery-3.6.0.min.js',
            settings.STATIC_URL + 'admin/js/media.js',
        ]
        css = {
            'all': (settings.STATIC_URL + 'admin/css/media.css',)
        }

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'my_media_field':
            url = formfield.widget.attrs.get('data-url', '')
            widget_html = formfield.widget.render(name=db_field.name, value=formfield.value())
            return format_html('<div class="related-widget-wrapper"><a href="{}" class="file-upload">{}</a> {}</div>', url, 'Upload a new file', widget_html)
        return formfield