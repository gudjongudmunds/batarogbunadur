from django.contrib import admin

from .models import Batar, BatarFyrirspurn, Batategund, Batahradi, Batavel, Batagerd, Att, Stadsetning, Svaedi, Smidastod, Efnibol, Heimahofn

# Register your models here.

class BatarAdmin(admin.ModelAdmin):
    list_filter= ('birta','tegund',)
    list_display= ('nafn','nr','nyskr_dags','rodun','uppf_dags','birta',)
    prepopulated_fields= {'slug': ['nr','nafn']}

class BatarFyrirspurnAdmin(admin.ModelAdmin):
    list_display= ('skrdags','nafn','tengil_nafn','svarad',)

admin.site.register(Batar, BatarAdmin)
admin.site.register(BatarFyrirspurn, BatarFyrirspurnAdmin)
admin.site.register(Batategund)
admin.site.register(Batahradi)
admin.site.register(Batagerd)
admin.site.register(Batavel)
admin.site.register(Att)
admin.site.register(Stadsetning)
admin.site.register(Svaedi)
admin.site.register(Smidastod)
admin.site.register(Efnibol)
admin.site.register(Heimahofn)