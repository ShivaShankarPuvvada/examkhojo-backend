from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from exam.models import Exam


class College(models.Model):
    """Model for college."""

    class OwnershipChoices(models.IntegerChoices):
        """Choices for ownership."""
        PRIVATE = 0, _('Private')
        PUBLIC = 1, _('Public')
        OTHER = 2, _('Other')

    class InstitutionType(models.IntegerChoices):
        """Choices for Institution type."""
        GRADUATION_COLLEGE = 0,
        DIPLOMA_COLLEGE = 1,
        VOCATIONAL_TRAINING = 2

    full_name = models.CharField(max_length=255)
    abbreviated_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    brochure = models.FileField(upload_to='college/brochure/')
    image = models.ImageField(upload_to='college/image/')
    logo = models.ImageField(upload_to='college/logo/')
    ownership = models.IntegerField(choices=OwnershipChoices.choices)
    approval = models.CharField(max_length=100)
    college_type = models.IntegerField(choices=InstitutionType.choices)
    date_of_establishment = models.DateField(null=True)
    slug = models.SlugField(max_length=50)
    about = models.TextField(null=True)
    is_top = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.full_name)
        super(College, self).save(*args, **kwargs)


class EntranceExam(models.Model):
    """Specify which entrance exams for which college."""

    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE)


class Degree(models.Model):
    """Model of degrees."""

    full_name = models.CharField(max_length=255)
    abbreviated_name = models.CharField(max_length=50)


class Stream(models.Model):
    """Model for streams."""

    class DegreeType(models.Choices):
        """Types of degree."""
        UNDER_GRADUATE = 'UG'
        POST_GRADUATE = 'PG'
        DIPLOMA = 'D'
        DOCTORATE = 'PHD'
        OTHERS = 'OT'

    name = models.CharField(max_length=60)
    degree_type = models.CharField(max_length=3, choices=DegreeType.choices)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, null=True)


class StreamCollegeMap(models.Model):
    """Map college with stream."""
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE)


class OfficialContact(models.Model):
    """Model to store official college contacts."""

    college = models.ForeignKey(College, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=40, null=True)
    full_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
