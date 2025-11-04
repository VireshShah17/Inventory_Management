from django.db import models
from common.models import BaseModel
from party.models import Party

# Create your models here.
class ProductCategory(BaseModel):
    category_id = models.AutoField(primary_key = True)
    category_name = models.CharField(max_length = 100, unique = True)
    description = models.TextField(blank = True, null = True)
    parent_category = models.ForeignKey('self', on_delete = models.CASCADE, blank = True, null = True, related_name = 'subcategories')


    def __str__(self):
        return self.category_name
    

class Product(BaseModel):
    PRODUCT_TYPES = [
        ("AGGREGATED", "Configurable Good"),
        ("AGGREGATED_CONF", "Configurable Good Configuration"),
        ("ASSET_USAGE", "Fixed Asset Usage"),
        ("DIGITAL_GOOD", "Digital Good"),
        ("FINDIG_GOOD", "Finished/Digital Good"),
        ("FINISHED_GOOD", "Finished Good"),
        ("GOOD", "Good"),
        ("MARKETING_PKG_PICK", "Marketing Package: Pick Assembly"),
        ("MARKETING_PKG_AUTO", "Marketing Package: Auto Manufactured"),
        ("RAW_MATERIAL", "Raw Material"),
        ("SERVICE", "Service"),
        ("SUBASSEMBLY", "Subassembly"),
        ("WIP", "Work in Progress"),
    ]

    UOM_CHOICES = [
        ("EA", "Each"),
        ("KG", "Kilogram"),
        ("LB", "Pound"),
        ("M", "Meter"),
        ("CM", "Centimeter"),
        ("L", "Liter"),
        ("GAL", "Gallon"),
        ("HOUR", "Hour"),
    ]

    product_id = models.AutoField(primary_key = True)
    product_name = models.CharField(max_length = 200, unique = True)
    description = models.TextField(blank = True, null = True)
    product_type = models.CharField(max_length = 20, choices = PRODUCT_TYPES)
    internal_name = models.CharField(max_length = 200, blank = True, null = True)
    uom = models.CharField(max_length = 10, choices = UOM_CHOICES)
    is_active = models.BooleanField(default = True)
    created_by = models.ForeignKey(Party, on_delete = models.SET_NULL, blank = True, null = True, related_name = 'products_created')


    def __str__(self):
        return f"{self.product_name} ({self.product_type})"


class ProductCategoryMember(BaseModel):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = 'category_memberships')
    category = models.ForeignKey(ProductCategory, on_delete = models.CASCADE, related_name = 'product_members')
    from_date = models.DateField()
    thru_date = models.DateField(blank = True, null = True)


    class Meta:
        unique_together = ('product', 'category')


    def __str__(self):
        return f"{self.product.product_name} in {self.category.category_name}"


class GoodIdentification(BaseModel):
    IDENTIFIER_TYPES = [
        ('SKU', 'Stock Keeping Unit'),
        ('BARCODE', 'Barcode'),
        ('EAN', 'EAN Code'),
        ('QR', 'QR Code'),
    ]
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='identifications')
    good_identification_type = models.CharField(max_length=20, choices=IDENTIFIER_TYPES)
    id_value = models.CharField(max_length=100, unique=True)
    from_date = models.DateField()
    thru_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.good_identification_type}: {self.id_value}"


class ProductPrice(BaseModel):
    PRICE_TYPES = [
        ('DEFAULT_PRICE', 'Default Price'),
        ('DISCOUNT_PRICE', 'Discounted Price'),
        ('WHOLESALE_PRICE', 'Wholesale Price'),
    ]

    CURRENCY_CHOICES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('GBP', 'British Pound'),
        ('JPY', 'Japanese Yen'),
        ('INR', 'Indian Rupee'),
        ('CNY', 'Chinese Yuan'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices')
    price_type = models.CharField(max_length=20, choices=PRICE_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES)
    from_date = models.DateField()
    thru_date = models.DateField(blank=True, null=True)


    def __str__(self):
        return f"{self.product.product_name} - {self.price_type}: {self.amount} {self.currency}"
