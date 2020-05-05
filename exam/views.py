from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from exam.models import Exam, ExamDate, ExamCutoff


def get_exams(request):
    """Get the exams."""
    page = request.GET.get('page', 1)
    search_string = request.GET.get('q', None)
    if search_string:
        exam_list = Exam.objects.filter(
            full_name__icontains=search_string
        ).order_by('full_name')
    else:
        exam_list = Exam.objects.all().order_by('full_name')

    paginator = Paginator(exam_list, 9)
    try:
        exams = paginator.page(page)
    except PageNotAnInteger:
        exams = paginator.page(1)
    except EmptyPage:
        exams = paginator.page(paginator.num_pages)
    return render(
        request,
        'pages/exams.html',
        {
            'exams': exams
        }
    )


def get_single_exam(request, exam_slug):
    """Get single exam."""
    exam = Exam.objects.filter(slug=exam_slug).first()
    dates = ExamDate.objects.filter(
        exam=exam
    )
    cutoffs = ExamCutoff.objects.filter(
        exam=exam
    )
    return render(
        request,
        'pages/individual-exam.html',
        {
            'exam': exam,
            'dates': dates,
            'cutoffs': cutoffs
        }
    )
