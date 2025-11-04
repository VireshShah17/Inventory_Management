from rest_framework import viewsets, serializers
from .models import (
    Party,
    Person,
    PartyGroup,
    PartyRole,
    ContactMech,
    TelecomNumber,
    PostalAddress,
    PartyContactMech,
)


# -------------------------------
# SERIALIZERS
# -------------------------------

class ContactMechSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMech
        fields = '__all__'


class TelecomNumberSerializer(serializers.ModelSerializer):
    contact_mech = ContactMechSerializer(read_only=True)

    class Meta:
        model = TelecomNumber
        fields = '__all__'


class PostalAddressSerializer(serializers.ModelSerializer):
    contact_mech = ContactMechSerializer(read_only=True)

    class Meta:
        model = PostalAddress
        fields = '__all__'


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    party = PartySerializer(read_only=True)

    class Meta:
        model = Person
        fields = '__all__'


class PartyGroupSerializer(serializers.ModelSerializer):
    party = PartySerializer(read_only=True)

    class Meta:
        model = PartyGroup
        fields = '__all__'


class PartyRoleSerializer(serializers.ModelSerializer):
    party = PartySerializer(read_only=True)

    class Meta:
        model = PartyRole
        fields = '__all__'


class PartyContactMechSerializer(serializers.ModelSerializer):
    party = PartySerializer(read_only=True)
    contact_mech = ContactMechSerializer(read_only=True)

    class Meta:
        model = PartyContactMech
        fields = '__all__'


# -------------------------------
# VIEWSETS
# -------------------------------

class PartyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PartySerializer


class PersonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Person.objects.all().select_related('party')
    serializer_class = PersonSerializer


class PartyGroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PartyGroup.objects.all().select_related('party')
    serializer_class = PartyGroupSerializer


class PartyRoleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PartyRole.objects.all().select_related('party')
    serializer_class = PartyRoleSerializer


class ContactMechViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ContactMech.objects.all()
    serializer_class = ContactMechSerializer


class TelecomNumberViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TelecomNumber.objects.all().select_related('contact_mech')
    serializer_class = TelecomNumberSerializer


class PostalAddressViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PostalAddress.objects.all().select_related('contact_mech')
    serializer_class = PostalAddressSerializer


class PartyContactMechViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PartyContactMech.objects.all().select_related('party', 'contact_mech')
    serializer_class = PartyContactMechSerializer


