from django.contrib import admin

from .models import Aflaheim, AflaheimFyrirspurn, Tegundaflah, Tegundsjavaraf

# Register your models here.

class AflaheimAdmin(admin.ModelAdmin):
    list_filter= ('birta','tegundaflah',)
    list_display= ('nafn','nyskr_dags','rodun','uppf_dags','birta',)
    prepopulated_fields= {'slug': ['nafn']}
    
class AflaheimFyrirspurnAdmin(admin.ModelAdmin):
    list_display= ('skrdags','nafn','tengil_nafn','svarad',)

admin.site.register(Aflaheim, AflaheimAdmin)
admin.site.register(AflaheimFyrirspurn, AflaheimFyrirspurnAdmin)
admin.site.register(Tegundaflah)
admin.site.register(Tegundsjavaraf)
