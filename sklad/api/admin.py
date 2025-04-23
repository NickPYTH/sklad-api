from django.contrib import admin

from .models import Supplier, Employee, Supply, Category, Material, SupplyMaterial, InventoryStatus, Inventory, \
    Requirement

admin.site.site_header = "Даркстор схема"


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("title", "fio", "phone")
    search_fields = ("title", "fio", "phone")
    list_filter = ("title", "fio", "phone")


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("fio", "post", "phone")
    search_fields = ("fio", "post", "phone")
    list_filter = ("fio", "post", "phone")


@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "createDateTime", "receiveDateTime", "employee", "supplier")
    search_fields = ("name", "description", "createDateTime", "receiveDateTime")
    list_filter = ("name", "description", "createDateTime", "receiveDateTime", "employee", "supplier")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", )
    search_fields = ("name", )
    list_filter = ("name", )


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "number")
    search_fields = ("name", "description", "number")
    list_filter = ("name", "description", "number")


@admin.register(SupplyMaterial)
class SupplyMaterial(admin.ModelAdmin):
    pass


@admin.register(InventoryStatus)
class InventoryStatusAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ("name", "count")
    search_fields = ("name", "count")
    list_filter = ("name", "count")