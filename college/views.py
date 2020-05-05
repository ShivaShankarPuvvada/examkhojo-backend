from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from college.models import College, EntranceExam, StreamCollegeMap, OfficialContact


def get_colleges(request):
    """Get the colleges."""
    page = request.GET.get('page', 1)
    search_string = request.GET.get('q', None)
    if search_string:
        college_list = College.objects.filter(
            full_name__icontains=search_string
        ).order_by('full_name')
    else:
        college_list = College.objects.all().order_by('full_name')

    paginator = Paginator(college_list, 9)
    try:
        colleges = paginator.page(page)
    except PageNotAnInteger:
        colleges = paginator.page(1)
    except EmptyPage:
        colleges = paginator.page(paginator.num_pages)
    return render(
        request,
        'pages/colleges.html',
        {
            'colleges': colleges
        }
    )


def get_single_college(request, college_slug):
    """Get single college."""
    college = College.objects.filter(slug=college_slug).first()
    exams = EntranceExam.objects.filter(
        college=college
    )
    streams = StreamCollegeMap.objects.filter(
        college=college
    ).order_by('stream__name')
    degrees = streams.distinct('stream__degree__abbreviated_name')
    streams = [{
        'stream_1': streams[index].stream.name,
        'stream_2': streams[index + 1].stream.name
    } for index, stream in enumerate(streams) if index % 2 != 0]
    contacts = OfficialContact.objects.filter(
        college=college
    )
    return render(
        request,
        'pages/individual-college.html',
        {
            'college': college,
            'exams': exams,
            'degrees': degrees,
            'streams': streams,
            'contacts': contacts
        }
    )
