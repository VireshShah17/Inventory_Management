from django.contrib import admin
from .models import (
    Party,
    Person,
    PartyGroup,
    PartyRole,
    PartyContactMech,
    ContactMech,
    TelecomNumber,
    PostalAddress,
)

# -------------------------------
# PARTY ADMIN
# -------------------------------
@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = ('party_id', 'party_type', 'external_id', 'is_active', 'created_at', 'updated_at')
    search_fields = ('party_id', 'external_id', 'party_type')
    list_filter = ('party_type', 'is_active')
    ordering = ('-updated_at',)


# -------------------------------
# PERSON ADMIN
# -------------------------------
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('party', 'first_name', 'last_name', 'date_of_birth', 'gender', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'party__party_id')
    list_filter = ('gender',)
    ordering = ('first_name',)


# -------------------------------
# PARTY GROUP ADMIN
# -------------------------------
@admin.register(PartyGroup)
class PartyGroupAdmin(admin.ModelAdmin):
    list_display = ('party', 'group_name', 'description', 'created_at', 'updated_at')
    search_fields = ('group_name', 'party__party_id')
    ordering = ('group_name',)


# -------------------------------
# PARTY ROLE ADMIN
# -------------------------------
@admin.register(PartyRole)
class PartyRoleAdmin(admin.ModelAdmin):
    list_display = ('party', 'role_type', 'start_date', 'end_date', 'created_at', 'updated_at')
    search_fields = ('role_type', 'party__party_id')
    list_filter = ('role_type',)
    ordering = ('-start_date',)


# -------------------------------
# CONTACT MECH ADMIN
# -------------------------------
@admin.register(ContactMech)
class ContactMechAdmin(admin.ModelAdmin):
    list_display = ('contact_mech_id', 'contact_mech_type', 'info_string', 'created_at', 'updated_at')
    search_fields = ('contact_mech_id', 'info_string', 'contact_mech_type')
    list_filter = ('contact_mech_type',)
    ordering = ('contact_mech_type',)


# -------------------------------
# TELECOM NUMBER ADMIN
# -------------------------------
@admin.register(TelecomNumber)
class TelecomNumberAdmin(admin.ModelAdmin):
    list_display = ('contact_mech', 'country_code', 'area_code', 'number', 'extension', 'created_at', 'updated_at')
    search_fields = ('contact_mech__contact_mech_id', 'number')
    ordering = ('contact_mech',)


# -------------------------------
# POSTAL ADDRESS ADMIN
# -------------------------------
@admin.register(PostalAddress)
class PostalAddressAdmin(admin.ModelAdmin):
    list_display = ('contact_mech', 'address_line1', 'city', 'state_province', 'postal_code', 'country', 'created_at', 'updated_at')
    search_fields = ('contact_mech__contact_mech_id', 'city', 'state_province', 'postal_code')
    list_filter = ('country',)
    ordering = ('country', 'city')


# -------------------------------
# PARTY CONTACT MECH ADMIN
# -------------------------------
@admin.register(PartyContactMech)
class PartyContactMechAdmin(admin.ModelAdmin):
    list_display = ('party', 'contact_mech', 'purpose_type', 'from_date', 'thru_date', 'created_at', 'updated_at')
    search_fields = ('party__party_id', 'contact_mech__contact_mech_id', 'purpose_type')
    list_filter = ('purpose_type',)
    ordering = ('party', 'purpose_type')
