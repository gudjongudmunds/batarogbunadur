from django.contrib import admin

from .models import Fyrirspurn
from .models import PageVisit
# Register your models here.


class FyrirspurnAdmin(admin.ModelAdmin):
    list_display= ('dags','titill','nafn','svarad',)

@admin.register(PageVisit)
class PageVisitAdmin(admin.ModelAdmin):
    list_display = ('url', 'visit_count')
    search_fields = ('url',)


admin.site.register(Fyrirspurn, FyrirspurnAdmin)