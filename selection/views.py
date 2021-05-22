from django.utils.translation import ugettext_lazy as _
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
from .serializers import (
        CandidateSerializer,
        ContactSerializer,
        ContactCandidateSerializer
    )

from .models import Candidate, Contact
# Create your views here.

class CandidateViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()

    @action(
        methods=['post'],
        url_path='contact',
        detail=True        
    )
    def add_contact(self, request, pk=None):
        """
        post:
        Create a contact into candidate
        """
        try:
            candidate = Candidate.objects.get(pk=pk)
            serializer = ContactCandidateSerializer(
                data=request.data, context={'candidate': candidate}
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Candidate.DoesNotExist:
            return Response({
                'id':_("Candidate not found!")
            }, status=status.HTTP_404_NOT_FOUND)

class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()