from django.contrib import admin

from .models import Gallery, Fyrirspurn

# Register your models here.

class FyrirspurnAdmin(admin.ModelAdmin):
    list_filter= ('dags',)
    list_display= ('dags','nafn',)

class GalleryAdmin(admin.ModelAdmin):
    list_filter= ('titill','date',)
    list_display= ('titill','date',)
    prepopulated_fields= {"slug": ["titill"]}

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Fyrirspurn, FyrirspurnAdmin)