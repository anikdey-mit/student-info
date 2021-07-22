from django.shortcuts import render
from student_information import forms
from student_information.models import Student

# Create your views here.
def index(request):
    student_list = Student.objects.order_by('name')
    context = {'title': 'Student Information - Home',
               'student_list': student_list}
    return render(request, 'index.html', context)


def form(request):
    form = forms.StudentForm()

    if request.method == "POST":
        form = forms.StudentForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return index(request)
    
    context = {'title': 'Student Form', 'student_form': form}
    return render(request, 'student_form.html', context)

def details(request,student_id):
    details = Student.objects.get(pk=student_id)
    context = {'details': details}
    return render(request, 'student_details.html',context)


def update(request, student_id):
    details = Student.objects.get(pk=student_id)
    form = forms.StudentForm(instance = details)

    if request.method == "POST":
        form = forms.StudentForm(request.POST, instance=details)

        if form.is_valid():
            form.save(commit=True)
            #return index(request)
            details = Student.objects.get(pk=student_id)
            context = {'details': details}
            return render(request, 'student_details.html', context)

    context = {'student_form': form}
    return render(request, 'student_update.html', context)


def delete(request, student_id):
    student = Student.objects.get(pk=student_id).delete()
    context = {'delete_message' : "Delete Done!!!"}
    return render(request, 'student_delete.html', context)
