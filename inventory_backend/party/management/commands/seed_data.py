from django.core.management.base import BaseCommand
from party.models import Party, Person, PartyRole, ContactMech, TelecomNumber, PostalAddress, PartyContactMech
from faker import Faker
import random
from datetime import date

class Command(BaseCommand):
    help = "Seed demo data for Party and related models"

    def handle(self, *args, **kwargs):
        fake = Faker()
        Faker.seed(42)

        # --- Create Demo Customers ---
        for _ in range(10):
            # Create Party
            party = Party.objects.create(
                party_type="PERSON",
                external_id=fake.uuid4(),
                is_active=True,
            )

            # Create Person details
            person = Person.objects.create(
                party=party,
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                gender=random.choice(["Male", "Female"]),
                date_of_birth=fake.date_of_birth(minimum_age=18, maximum_age=60),
            )

            # Assign role as CUSTOMER
            PartyRole.objects.create(
                party=party,
                role_type="CUSTOMER",
                start_date=date.today(),
            )

            # Create ContactMech (Email + Phone + Address)
            email_mech = ContactMech.objects.create(
                contact_mech_type="EMAIL_ADDRESS",
                info_string=fake.email(),
            )
            phone_mech = ContactMech.objects.create(
                contact_mech_type="TELECOM_NUMBER",
                info_string=fake.phone_number(),
            )
            address_mech = ContactMech.objects.create(
                contact_mech_type="POSTAL_ADDRESS",
                info_string=f"{fake.street_address()}, {fake.city()}",
            )

            # Telecom details
            TelecomNumber.objects.create(
                contact_mech=phone_mech,
                number=fake.msisdn(),
                country_code="+91",
            )

            # Postal address details
            PostalAddress.objects.create(
                contact_mech=address_mech,
                address_line1=fake.street_address(),
                city=fake.city(),
                state_province=fake.state(),
                postal_code=fake.postcode(),
                country="India",
            )

            # PartyContactMech associations
            PartyContactMech.objects.create(
                party=party,
                contact_mech=email_mech,
                purpose_type="PRIMARY_EMAIL",
                from_date=date.today(),
            )
            PartyContactMech.objects.create(
                party=party,
                contact_mech=phone_mech,
                purpose_type="PRIMARY_PHONE",
                from_date=date.today(),
            )
            PartyContactMech.objects.create(
                party=party,
                contact_mech=address_mech,
                purpose_type="PRIMARY_LOCATION",
                from_date=date.today(),
            )

        self.stdout.write(self.style.SUCCESS("✅ Demo Party and Person data created successfully!"))
