from django.contrib import admin
from .models import InventoryItem, InventoryItemDetails


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = (
        "inventory_item_id",
        "product",
        "quantity_on_hand",
        "quantity_reserved",
        "status",
        "facility",
        "lot_number",
        "created_at",
        "updated_at",
    )
    search_fields = ("product__product_name", "facility", "lot_number")
    list_filter = ("status", "facility")


@admin.register(InventoryItemDetails)
class InventoryItemDetailAdmin(admin.ModelAdmin):
    list_display = (
        "inventory_item",
        "transaction_type",
        "quantity",
        "transaction_date",
        "performed_by",
    )
    list_filter = ("transaction_type",)
    search_fields = ("inventory_item__product__product_name", "performed_by__party_id")
