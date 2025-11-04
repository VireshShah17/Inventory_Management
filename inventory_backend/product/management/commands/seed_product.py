from django.core.management.base import BaseCommand
from product.models import (
    Product,
    ProductCategory,
    ProductCategoryMember,
    GoodIdentification,
    ProductPrice,
)
from party.models import Party
from faker import Faker
import random
from datetime import date, timedelta


class Command(BaseCommand):
    help = "Seed demo data for Products, Categories, SKUs, and Prices"

    def handle(self, *args, **kwargs):
        fake = Faker()
        Faker.seed(42)

        # Clean up old data
        ProductPrice.objects.all().delete()
        GoodIdentification.objects.all().delete()
        ProductCategoryMember.objects.all().delete()
        Product.objects.all().delete()
        ProductCategory.objects.all().delete()

        self.stdout.write(self.style.WARNING("⚙️ Existing product data cleared."))

        # Get one Party as creator (if exists)
        creator = Party.objects.first()

        # --- Create Product Categories ---
        categories = []
        category_names = [
            "Electronics",
            "Groceries",
            "Furniture",
            "Clothing",
            "Stationery",
            "Sports",
            "Beauty & Health",
        ]
        for name in category_names:
            cat = ProductCategory.objects.create(
                category_name=name,
                description=fake.sentence(),
            )
            categories.append(cat)
        self.stdout.write(self.style.SUCCESS(f"✅ {len(categories)} Product Categories created."))

        # --- Create Products ---
        products = []
        for _ in range(30):
            category = random.choice(categories)
            prod_type = random.choice([t[0] for t in Product.PRODUCT_TYPES])
            uom = random.choice([u[0] for u in Product.UOM_CHOICES])

            product = Product.objects.create(
                product_name=fake.unique.word().capitalize() + " " + category.category_name,
                description=fake.sentence(),
                product_type=prod_type,
                internal_name=fake.slug(),
                uom=uom,
                created_by=creator,
                is_active=True,
            )
            products.append(product)

            # Link product to category
            ProductCategoryMember.objects.create(
                product=product,
                category=category,
                from_date=date.today(),
            )

            # Create SKUs / Barcodes
            sku_type = random.choice(["SKU", "BARCODE", "QR"])
            GoodIdentification.objects.create(
                product=product,
                good_identification_type=sku_type,
                id_value=fake.unique.ean(length=13),
                from_date=date.today(),
            )

            # Create Prices
            ProductPrice.objects.create(
                product=product,
                price_type="DEFAULT_PRICE",
                amount=round(random.uniform(100, 5000), 2),
                currency="INR",
                from_date=date.today(),
            )

        self.stdout.write(self.style.SUCCESS(f"✅ {len(products)} Products with identifiers and prices created successfully!"))
