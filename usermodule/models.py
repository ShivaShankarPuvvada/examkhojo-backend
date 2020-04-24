from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    """Profile class based on top of user."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField()
    display_pic = models.ImageField(upload_to='user/dp/')
    mobile_number = models.CharField(max_length=20)
    full_name = models.CharField(max_length=100)


class OTPVerification(models.Model):
    """OTP Verification stack trace."""

    class VerifierTag(models.IntegerChoices):
        """Reason for generating OTP."""
        MAIL_VERIFICATION = 1, _('MAIL VERIFICATION')
        PHONE_VERIFICATION = 2, _('PHONE VERIFICATION')
        PASSWORD_RESET = 3, _('PASSWORD RESET')
        OTHER = 0, _('Other')

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    verifier_tag = models.IntegerField(choices=VerifierTag.choices)
    is_verified = models.SmallIntegerField(default=0)

