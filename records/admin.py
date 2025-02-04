from django.contrib import admin
from .models import Record, RecordType
# Register your models here.

# admin.site.register(Record)
@admin.register(RecordType)
class RecordTypeAdmin(admin.ModelAdmin):
    list_display = ( "name",)
    list_filter = ("name",)
    search_fields = ("name",)
    

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ("record_type", "value")
    autocomplete_fields = ("player","record_type",)
    # list_filter = ()
    
    