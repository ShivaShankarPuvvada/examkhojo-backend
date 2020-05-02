from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Exam(models.Model):
    """Model for exams."""

    class ExamLevel(models.Choices):
        """Types of exam level."""
        NATIONAL = 'NT'
        INTERNATIONAL = 'INT'
        STATE = 'ST'
        DISTRICT = 'DT'

    class BasicEligibilityChoices(models.IntegerChoices):
        """Eligibility choices."""
        TEN = 1, _('Metric Pass')
        TWELVE = 2, _('HS Pass')
        UNDER_GRADUATE = 3, _('Under Graduate')
        POST_GRADUATE = 4, _('Post Graduate')
        OTHER = 0, _('Other')

    full_name = models.CharField(max_length=200)
    abbreviated_name = models.CharField(max_length=200)
    conducting_body_full_name = models.CharField(max_length=200)
    conducting_body_abbreviated_name = models.CharField(max_length=200)
    official_website = models.CharField(max_length=200)
    tentative_date = models.DateField()
    exam_level = models.CharField(max_length=5, choices=ExamLevel.choices)
    eligibility = models.IntegerField(choices=BasicEligibilityChoices.choices)
    document = models.FileField(upload_to='exams/documents/')
    about = models.TextField()
    cutoff_details = models.TextField()
    slug = models.SlugField(max_length=50)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.full_name)
        super(Exam, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name
