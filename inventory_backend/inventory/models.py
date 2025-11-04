from django.db import models
from common.models import BaseModel
from product.models import Product
from party.models import Party

# Create your models here.
class InventoryItem(BaseModel):
    STATUS_CHOICES = [
        ('AVAILABLE', 'Available'),
        ('RESERVED', 'Reserved'),
        ('SOLD', 'Sold'),
        ('RETURNED', 'Returned'),
        ('DAMAGED', 'Damaged'),
    ]

    inventory_item_id = models.AutoField(primary_key = True)
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = 'inventory_items')
    quantity_on_hand = models.PositiveIntegerField()
    quantity_reserved = models.PositiveIntegerField(default = 0)
    status = models.CharField(max_length = 20, choices = STATUS_CHOICES, default = 'AVAILABLE')
    facility = models.CharField(max_length = 100, blank = True, null = True)  # warehouse/store location
    lot_number = models.CharField(max_length = 50, blank = True, null = True)
    owner_party = models.ForeignKey(
        Party, on_delete=models.SET_NULL, null = True, blank = True, related_name = 'owned_inventory'
    )
    expiration_date = models.DateField(blank = True, null = True)

    def __str__(self):
        return f"InventoryItem {self.inventory_item_id} - {self.product.name} - Status: {self.status}"
    

class InventoryItemDetails(BaseModel):
    TRANSACTION_TYPE_CHOICES = [
        ('RECEIPT', 'Receipt In'),
        ('SALE', 'Sale Out'),
        ('RETURN', 'Return In'),
        ('ADJUSTMENT', 'Stock Adjust'),
    ]

    inventory_item = models.ForeignKey(InventoryItem, on_delete = models.CASCADE, related_name = 'details')
    transaction_type = models.CharField(max_length = 20, choices = TRANSACTION_TYPE_CHOICES)
    quantity = models.DecimalField(max_digits = 10, decimal_places = 2)
    transaction_date = models.DateTimeField(auto_now_add = True)
    reason = models.TextField(blank = True, null = True)
    performed_by = models.ForeignKey(
        Party, on_delete=models.SET_NULL, null = True, blank = True, related_name = 'inventory_actions'
    )

    def __str__(self):
        return f"{self.transaction_type}: {self.quantity} ({self.inventory_item.product.product_name})"
