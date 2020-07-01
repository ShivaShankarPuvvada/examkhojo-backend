from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class Course(models.Model):
    """Class for exams."""

    class StreamChoices(models.IntegerChoices):
        """Streams available."""

        ENGINEERING = 1
        MEDICAL = 2
        HUMANITIES = 3
        FINANCE = 4
        ARTS = 5
        SCIENCE = 6
        OTHER = 0

    class LevelType(models.Choices):
        """Types of degree."""
        UNDER_GRADUATE = 'UG'
        POST_GRADUATE = 'PG'
        DIPLOMA = 'D'
        DOCTORATE = 'PHD'
        OTHERS = 'OT'

    class BasicEligibilityChoices(models.IntegerChoices):
        """Eligibility choices."""
        TEN = 1, _('Matric Pass')
        TWELVE = 2, _('HS Pass')
        UNDER_GRADUATE = 3, _('Under Graduate')
        POST_GRADUATE = 4, _('Post Graduate')
        OTHER = 0, _('Other')

    class ExaminationType(models.Choices):
        """Types of degree."""
        SEMESTER = 'SM'
        ANNUAL = 'AN'
        WEEKLY = 'WK'
        PATENT = 'PT'
        PAPER = 'PP'
        OTHER = 'OT'

    full_name = models.CharField(null=True, max_length=200)
    abbreviated_name = models.CharField(null=True, max_length=200)
    meta = models.TextField(null=True)
    keywords = models.TextField(null=True)
    stream = models.IntegerField(null=True, choices=StreamChoices.choices)
    level = models.CharField(null=True, max_length=5, choices=LevelType.choices)
    duration = models.CharField(null=True, max_length=100)
    eligibility = models.IntegerField(null=True, choices=BasicEligibilityChoices.choices)
    exam = models.CharField(null=True, max_length=3, choices=ExaminationType.choices)
    average_course_fee = models.CharField(null=True, max_length=20)
    about = models.TextField(null=True)
    syllabus_csv = models.TextField(null=True) #CSV field
    top_companies = models.TextField(null=True) #CSV field
    jobs = models.TextField(null=True) #CSV field
    slug = models.SlugField(null=True, max_length=50)
    is_top = models.BooleanField(null=True, default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.full_name)
        super(Course, self).save(*args, **kwargs)


class Job(models.Model):
    """Jobs available in industry."""

    name = models.CharField(null=True, max_length=100)


class CourseJob(models.Model):
    """Course job mapping."""

    degree = models.ForeignKey(Course, on_delete=models.PROTECT)
    job = models.ForeignKey(Job, on_delete=models.PROTECT)


class FAQCourse(models.Model):
    """FAQ model for every course."""

    question = models.TextField(null=True )
    answers = models.TextField(null=True )


class FAQLinkCourse(models.Model):
    """Link FAQ to courses."""

    faq = models.ForeignKey(FAQCourse, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
