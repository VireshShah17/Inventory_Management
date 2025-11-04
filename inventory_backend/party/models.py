from django.db import models
from common.models import BaseModel

# Create your models here.
class Party(BaseModel):
    PARTY_TYPES = [ 
        ('PERSON', 'Person'), 
        ('PARTY_GROUP', 'Party Group'),
    ]

    party_id = models.AutoField(primary_key = True)
    party_type = models.CharField(max_length = 20, choices = PARTY_TYPES, default = 'PERSON')
    external_id = models.CharField(max_length = 100, blank = True, null = True)
    is_active = models.BooleanField(default = True)


    def __str__(self):
        return f"Party {self.party_id} - Type: {self.party_type}"


class Person(BaseModel):
    party = models.OneToOneField(Party, on_delete = models.CASCADE, related_name = 'person')
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    date_of_birth = models.DateField(blank = True, null = True)
    gender = models.CharField(max_length = 10, blank = True, null = True)


    def __str__(self):
        return f"Person {self.first_name} {self.last_name} (Party ID: {self.party.party_id})"


class PartyGroup(BaseModel):
    party = models.OneToOneField(Party, on_delete = models.CASCADE, related_name = 'party_group')
    group_name = models.CharField(max_length = 100)
    description = models.TextField(blank = True, null = True)


    def __str__(self):
        return f"Party Group {self.group_name} (Party ID: {self.party.party_id})"
    

class PartyRole(BaseModel):
    ROLE_TYPES = [
        ('CUSTOMER', 'Customer'),
        ('SUPPLIER', 'Supplier'),
        ('EMPLOYEE', 'Employee'),
        ('PARTNER', 'Partner'),
    ]

    party = models.ForeignKey(Party, on_delete = models.CASCADE, related_name = 'roles')
    role_type = models.CharField(max_length = 20, choices = ROLE_TYPES)
    start_date = models.DateField()
    end_date = models.DateField(blank = True, null = True)


    def __str__(self):
        return f"PartyRole {self.role_type} for Party ID: {self.party.party_id}"


class ContactMech(BaseModel):
    CONTACT_TYPES = [
        ('TELECOM_NUMBER', 'Telecom Number'),
        ('EMAIL_ADDRESS', 'Email Address'),
        ('POSTAL_ADDRESS', 'Postal Address'),
    ]

    contact_mech_id = models.AutoField(primary_key = True)
    contact_mech_type = models.CharField(max_length = 20, choices = CONTACT_TYPES)
    info_string = models.CharField(max_length = 255)


    def __str__(self):
        return f"ContactMech {self.contact_mech_type}: {self.info_string}"


class TelecomNumber(BaseModel):
    contact_mech = models.OneToOneField(ContactMech, on_delete = models.CASCADE, related_name = 'telecom_number')
    country_code = models.CharField(max_length = 5, blank = True, null = True)
    area_code = models.CharField(max_length = 10, blank = True, null = True)
    number = models.CharField(max_length = 20)
    extension = models.CharField(max_length = 10, blank = True, null = True)


    def __str__(self):
        return f"TelecomNumber: {self.number}"


class PostalAddress(BaseModel):
    contact_mech = models.OneToOneField(ContactMech, on_delete = models.CASCADE, related_name = 'postal_address')
    address_line1 = models.CharField(max_length = 100)
    address_line2 = models.CharField(max_length = 100, blank = True, null = True)
    city = models.CharField(max_length = 50)
    state_province = models.CharField(max_length = 50)
    postal_code = models.CharField(max_length = 20)
    country = models.CharField(max_length = 50)


    def __str__(self):
        return f"PostalAddress: {self.address_line1}, {self.city}"


class PartyContactMech(BaseModel):
    PURPOSE_TYPE_CHOICES = [
        ("BILLING_EMAIL", "Billing (AP) Email"),
        ("BILLING_LOCATION", "Billing (AP) Address"),
        ("FAX_NUMBER", "Main Fax Number"),
        ("FAX_NUMBER_SEC", "Secondary Fax Number"),
        ("GENERAL_LOCATION", "General Correspondence Address"),
        ("ORDER_EMAIL", "Order Notification Email Address"),
        ("OTHER_EMAIL", "Other Email Address"),
        ("PAYMENT_EMAIL", "Payment (AR) Email"),
        ("PAYMENT_LOCATION", "Payment (AR) Address"),
        ("PHONE_ASSISTANT", "Assistant's Phone Number"),
        ("PHONE_BILLING", "Billing (AP) Phone Number"),
        ("PHONE_DID", "Direct Inward Dialing Phone Number"),
        ("PHONE_HOME", "Main Home Phone Number"),
        ("PHONE_MOBILE", "Main Mobile Phone Number"),
        ("PHONE_PAYMENT", "Payment (AR) Phone Number"),
        ("PHONE_QUICK", "Quick Calls Phone Number"),
        ("PHONE_SHIP_ORIG", "Shipping Origin Phone Number"),
        ("PHONE_SHIPPING", "Shipping Destination Phone Number"),
        ("PHONE_WORK", "Main Work Phone Number"),
        ("PHONE_WORK_SEC", "Secondary Work Phone Number"),
        ("PREVIOUS_LOCATION", "Previous Address"),
        ("PRIMARY_EMAIL", "Primary Email Address"),
        ("PRIMARY_LOCATION", "Primary Address"),
        ("PRIMARY_PHONE", "Primary Phone Number"),
        ("PRIMARY_WEB_URL", "Primary Website URL"),
        ("PUR_RET_LOCATION", "Purchase Return Address"),
        ("SHIP_ORIG_LOCATION", "Shipping Origin Address"),
        ("SHIPPING_LOCATION", "Shipping Destination Address"),
    ]

    party = models.ForeignKey(Party, on_delete = models.CASCADE, related_name = 'contact_mechanisms')
    contact_mech = models.ForeignKey(ContactMech, on_delete = models.CASCADE, related_name = 'parties')
    purpose_type = models.CharField(max_length = 30, choices = PURPOSE_TYPE_CHOICES)
    from_date = models.DateField()
    thru_date = models.DateField(blank = True, null = True)

    def __str__(self):
        return f"PartyContactMech: Party ID {self.party.party_id} - ContactMech ID {self.contact_mech.contact_mech_id} - Purpose: {self.purpose_type}"

