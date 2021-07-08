from django.contrib import admin
from .models import NetworkList, AddSubList, NewExposure


class NetworkListAdmin(admin.ModelAdmin):
    
    list_display = (
        "id",
        "subnet_name",
        "subnet_value"
    )


class AddSubListAdmin(admin.ModelAdmin):
    
    list_display = (
        "id",
        "acc_subnet_name",
        "acc_subnet_value"
    )

admin.site.register(NetworkList, NetworkListAdmin)
admin.site.register(AddSubList, AddSubListAdmin)

@admin.register(NewExposure)
class NewExposureAdmin(admin.ModelAdmin):
    
    list_display = (
        "id",
        "new_sub_name",
        "new_sub_value"
    )