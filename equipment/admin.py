from django.contrib import admin
from equipment.models import *

admin.site.register(EquipmentClass)
admin.site.register(ComponentType)
#admin.site.register(EquipComponent)
#admin.site.register(Equipment)


class EquipmentInline(admin.TabularInline):
    model = Equipment
    extra = 1

class EquipTypeComponentInline(admin.TabularInline):
    model = EquipTypeComponent
    extra = 1

class EquipComponentInline(admin.TabularInline):
    model = EquipComponent
    extra = 1

class EquipmentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['barcode', 'equipment_type', 'is_active']}),
    ]
    inlines = [EquipComponentInline]
#    list_display = ('equipment_name', 'equipment_class', 'is_active')


class EquipmentTypeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['equipment_class', 'equipment_name', 'is_active']}),
    ]
    inlines = [EquipTypeComponentInline, EquipmentInline]
    list_display = ('equipment_name', 'equipment_class', 'is_active')


admin.site.register(EquipmentType, EquipmentTypeAdmin)
admin.site.register(Equipment, EquipmentAdmin)