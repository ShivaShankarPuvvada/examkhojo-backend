from django.db import models

from usermodule.models import Profile


class Lead(models.Model):
    """Leads or interested persons."""

    class LeadType(models.IntegerChoices):
        """Choices for lead."""
        OTHER = 0, _('Other')
        COURSE = 1, _('Course')
        EXAM = 3, _('Exam')
        COLLEGE = 2, _('College')

    class LeadStatus(models.IntegerChoices):
        """Choices for lead status."""
        OTHER = 0, _('Other')
        SUCCESSFUL = 1, _('Successful')
        CONTACTED = 3, _('Contacted')
        FAILED = 2, _('Failed')
        ON_HOLD = 4, _('On Hold')
        IN_PROGRESS = 5, _('In Progress')

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    mobile = models.CharField(null=True, blank=True, max_length=20)
    name = models.CharField(null=True, blank=True, max_length=80)
    email = models.CharField(null=True, blank=True, max_length=80)
    lead_type = models.IntegerField(null=True, choices=LeadType.choices)
    lead_description = models.TextField(null=True, blank=True)
    status = models.IntegerField(null=True, choices=LeadStatus.choices)

    def __str__(self):
        return '{} - {}'.format(self.name, self.profile.full_name)


class FootPrint(models.Model):
    """Model to log user footprinting in website."""

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    page = models.CharField(null=True, blank=True, max_length=200)
    visited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {}'.format(self.page, self.profile.full_name)
