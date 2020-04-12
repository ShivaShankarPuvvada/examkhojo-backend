from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """Profile class based on top of user."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField()
    display_pic = models.ImageField(upload_to='user/dp/')
    mobile_number = models.CharField(max_length=20)
