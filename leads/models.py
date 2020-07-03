from django.db import models

from usermodule.models import Profile


class Lead(models.Model):
    """Leads or interested persons."""

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)