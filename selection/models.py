from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract=True        

class Candidate(BaseModel):
    TYPE_DOCUMENT_CHOICES = (
        (_("CNPJ"), _("CNPJ")),
        (_("CPF"), _("CPF")),
        (_("RG"), _("RG")),
        (_("Outro"),_("Outro"))
    )

    name = models.CharField(_("Name"),max_length=255)
    sobrenome = models.CharField(_("Sobrenome"),max_length=255)
    document_type = models.CharField(_("Document Type"),max_length=5, choices=TYPE_DOCUMENT_CHOICES)
    document = models.CharField(_("Document"),max_length=50, unique=True)
    job = models.CharField(_("Job Name"),max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Candidate')
        verbose_name_plural = _('Candidates')


class Contact(BaseModel):
    TYPE_CHOICES = (
        ("comercial", "Comercial"),
        ("pessoal", "Pessoal"),
    )
    type = models.CharField(_("Contact Type"),max_length=12, choices=TYPE_CHOICES)
    number = models.CharField(_("Contact Type"),max_length=12)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = _('Contact')
        verbose_name_plural = _('Contacts')