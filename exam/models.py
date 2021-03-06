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

    full_name = models.CharField(null=True, max_length=200)
    abbreviated_name = models.CharField(null=True, max_length=200)
    meta = models.TextField(null=True)
    keywords = models.TextField(null=True)
    application_fee = models.CharField(null=True, blank=True, max_length=200)
    conducting_body_full_name = models.CharField(null=True, max_length=200)
    conducting_body_abbreviated_name = models.CharField(null=True, max_length=200)
    official_website = models.CharField(null=True, max_length=200)
    tentative_date = models.DateField(null=True, )
    exam_level = models.CharField(null=True, max_length=5, choices=ExamLevel.choices)
    eligibility = models.IntegerField(null=True, choices=BasicEligibilityChoices.choices)
    document = models.FileField(null=True, upload_to='exams/documents/')
    about = models.TextField(null=True, )
    cutoff_details = models.TextField(null=True, )
    slug = models.SlugField(null=True, max_length=50)
    is_top = models.BooleanField(null=True, default=False)
    quick_facts = models.TextField(null=True)
    exam_pattern = models.TextField(null=True)
    admit_card = models.CharField(null=True, max_length=200)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.full_name)
        super(Exam, self).save(*args, **kwargs)

    def __str__(self):
        return self.full_name


class ExamDate(models.Model):
    """Models for exam date."""

    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    event = models.CharField(null=True, max_length=255)
    primary_date = models.DateField(null=True, )
    secondary_date = models.DateField(null=True)


class ExamCutoff(models.Model):
    """Exam cutoff."""

    class CutoffCategory(models.Choices):
        """Types of cutoff caste level."""
        GENERAL = 'G'
        SCHEDULE_CASTE = 'SC'
        SCHEDULE_TRIBE = 'ST'
        OTHER_BACKWARD_CLASS = 'OBC'
        PWD = 'PWD'
        COMMON = 'CM'
        OTHER = 'OT'

    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    category = models.CharField(null=True, max_length=5, choices=CutoffCategory.choices)
    cutoff_marks_1 = models.FloatField(null=True, max_length=20)
    cutoff_year_1 = models.DateField(null=True, )
    cutoff_marks_2 = models.FloatField(null=True, max_length=20)
    cutoff_year_2 = models.DateField(null=True)
    cutoff_marks_3 = models.FloatField(null=True, max_length=20)
    cutoff_year_3 = models.DateField(null=True)