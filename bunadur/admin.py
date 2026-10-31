from django.contrib import admin

from .models import Bunadur, BunadurFyrirspurn, Tegundbun

# Register your models here.

class BunadurAdmin(admin.ModelAdmin):
    list_filter= ('birta','tegundbun',)
    list_display= ('nafn','nyskr_dags','rodun','uppf_dags','birta',)
    prepopulated_fields= {'slug': ['nafn']}

class BunadurFyrirspurnAdmin(admin.ModelAdmin):
    list_display= ('skrdags','nafn','tengil_nafn','svarad')

admin.site.register(Bunadur, BunadurAdmin)
admin.site.register(BunadurFyrirspurn, BunadurFyrirspurnAdmin)
admin.site.register(Tegundbun)

