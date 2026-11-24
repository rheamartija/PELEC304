
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Student


def student_list(request):
    search = request.GET.get('search', '')

    students = Student.objects.all().order_by('last_name')

    if search:
        students = students.filter(
            Q(student_id__icontains=search) |
            Q(first_name__icontains=search) |
            Q(last_name__icontains=search) |
            Q(course__icontains=search)
        )

    context = {
        'students': students,
        'total_students': Student.objects.count(),
        'enrolled_students': Student.objects.filter(
            enrollment_status='Enrolled'
        ).count(),
        'search': search,
    }

    return render(request, 'students/student_list.html', context)


def student_profile(request, pk):
    student = get_object_or_404(Student, pk=pk)

    return render(
        request,
        'students/student_profile.html',
        {'student': student}
    )
