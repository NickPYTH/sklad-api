from django.contrib import admin

from .models import Supplier, Employee, Supply, Material, Inventory
admin.site.site_header = "Даркстор схема"


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("fio", "post", "phone")
    search_fields = ("fio", "post", "phone")
    list_filter = ("fio", "post", "phone")


@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    pass


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    pass


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    pass