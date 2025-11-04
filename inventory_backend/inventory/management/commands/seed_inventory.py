from django.core.management.base import BaseCommand
from inventory.models import InventoryItem, InventoryItemDetails
from product.models import Product
from party.models import Party
from faker import Faker
import random
from datetime import datetime


class Command(BaseCommand):
    help = "Seed demo inventory items and transaction history"

    def handle(self, *args, **kwargs):
        fake = Faker()
        Faker.seed(42)

        # Clear old data
        InventoryItemDetails.objects.all().delete()
        InventoryItem.objects.all().delete()
        self.stdout.write(self.style.WARNING("⚙️ Existing inventory data cleared."))

        # Fetch products and parties
        products = list(Product.objects.all())
        owners = list(Party.objects.filter(is_active=True))
        if not products:
            self.stdout.write(self.style.ERROR("❌ No products found! Please seed products first."))
            return

        # Facilities to simulate multiple warehouses
        facilities = ["Indore Main Warehouse", "Delhi Store", "Mumbai Distribution", "Online Fulfillment"]

        total_items = 0
        total_transactions = 0

        for product in products:
            # Random stock quantity
            quantity = random.randint(20, 200)
            reserved = random.randint(0, 10)

            # Assign an owner (random supplier or company party)
            owner = random.choice(owners) if owners else None

            # Create InventoryItem
            inv_item = InventoryItem.objects.create(
                product=product,
                quantity_on_hand=quantity,
                quantity_reserved=reserved,
                status="AVAILABLE",
                facility=random.choice(facilities),
                lot_number=f"LOT-{fake.random_int(min=1000, max=9999)}",
                owner_party=owner,
            )

            total_items += 1

            # Create some movement details
            transaction_types = ["RECEIPT", "SALE", "RETURN", "ADJUSTMENT"]
            for _ in range(random.randint(2, 5)):
                qty = round(random.uniform(1, 20), 2)
                InventoryItemDetails.objects.create(
                    inventory_item=inv_item,
                    transaction_type=random.choice(transaction_types),
                    quantity=qty,
                    reason=fake.sentence(nb_words=5),
                    performed_by=owner,
                )
                total_transactions += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"✅ Seeded {total_items} inventory items with {total_transactions} transactions successfully!"
            )
        )
