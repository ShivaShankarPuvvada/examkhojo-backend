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

    full_name = models.CharField(null=True, max_length=255)
    abbreviated_name = models.CharField(null=True, max_length=50)
    meta = models.TextField(null=True)
    keywords = models.TextField(null=True)
    city = models.CharField(null=True, max_length=50)
    state = models.CharField(null=True, max_length=50)
    brochure = models.FileField(null=True, upload_to='college/brochure/')
    image = models.ImageField(null=True, upload_to='college/image/')
    logo = models.ImageField(null=True, upload_to='college/logo/')
    ownership = models.IntegerField(null=True, choices=OwnershipChoices.choices)
    approval = models.CharField(null=True, max_length=100)
    college_type = models.IntegerField(null=True, choices=InstitutionType.choices)
    established_year = models.CharField(null=True, max_length=100)
    slug = models.SlugField(null=True, max_length=50)
    about = models.TextField(null=True)
    is_top = models.BooleanField(null=True, default=False)
    quick_facts = models.TextField(null=True)
    admission_process = models.TextField(null=True)
    placements = models.TextField(null=True)
    degrees = models.TextField(null=True) #CSV field
    streams = models.TextField(null=True) #CSV field

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

    full_name = models.CharField(null=True, max_length=255)
    abbreviated_name = models.CharField(null=True, max_length=50)


class Stream(models.Model):
    """Model for streams."""

    class DegreeType(models.Choices):
        """Types of degree."""
        UNDER_GRADUATE = 'UG'
        POST_GRADUATE = 'PG'
        DIPLOMA = 'D'
        DOCTORATE = 'PHD'
        OTHERS = 'OT'

    name = models.CharField(null=True, max_length=60)
    degree_type = models.CharField(null=True, max_length=3, choices=DegreeType.choices)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE, null=True)


class StreamCollegeMap(models.Model):
    """Map college with stream."""
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE)


class OfficialContact(models.Model):
    """Model to store official college contacts."""

    college = models.ForeignKey(College, on_delete=models.CASCADE)
    phone = models.CharField(null=True, max_length=20)
    email = models.CharField(null=True, max_length=40)
    full_name = models.CharField(null=True, max_length=100)
    designation = models.CharField(null=True, max_length=50)


class Gallery(models.Model):
    """Model to store images of colleges."""

    college = models.ForeignKey(College, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='college/gallery/')

    def __str__(self):
        return self.college
