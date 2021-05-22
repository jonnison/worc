from rest_framework import serializers
from .models import Candidate, Contact
from django.db import transaction
from django.db.models import Max
from django.utils.translation import ugettext_lazy as _


class ContactCandidateSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Contact
        exclude = ["candidate"]

    def create(self, validated_data):
        contact = Contact.objects.create(
            candidate = self.context['candidate'],
            **validated_data
        )

        return contact

class ContactSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Contact
        fields = ["type","number","candidate","updated_at", "created_at"]

class CandidateSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    contacts = serializers.SerializerMethodField(read_only=True)
    updated_at_contact = serializers.SerializerMethodField(read_only=True)

    def get_contacts(self, obj):
        return ContactSerializer(obj.contact_set.all(), many=True).data
    
    def get_updated_at_contact(self, obj):
        updated_at_contact = obj.contact_set.all().aggregate(
            date=Max("updated_at")
        )
        return updated_at_contact["date"]

    class Meta:
        model = Candidate
        fields = [
            "id", "name", "sobrenome", "document", "document_type", "job", 
            "updated_at", "created_at", "updated_at_contact", "contacts"
        ]